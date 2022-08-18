from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.html import strip_tags
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from goldentravel.tours.forms import TourForm
from goldentravel.tours.models import Tours
from goldentravel.applications.models import Application, Payment, PaymentChoice

from django.template.loader import render_to_string
from goldentravel.utils.init_payment import send_request


def send_mail_converter(values: dict) -> str:
    html_content = render_to_string('pages/email.html', values)
    text_content = strip_tags(html_content)
    return text_content


def detail_view(request, *args, **kwargs):
    obj = Tours.objects.filter(pk=kwargs['pk']).first()

    if request.method == 'GET':
        return render(request, 'tour/detail.html', {"obj": obj,
                                                    "form": TourForm(obj)
                                                    })

    elif request.method == 'POST':
        obj = Tours.objects.filter(pk=kwargs['pk']).first()
        form = TourForm(obj, request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            fullname = form.cleaned_data['fullname']
            application_obj = Application.objects.create(tour=obj, email=email, fullname=fullname)
            payment_url: str = send_request(application_obj)
            return HttpResponseRedirect(payment_url)
        else:
            return render(request, 'tour/detail.html', {"obj": obj, "form": form})


def failure(request):
    order_id = request.GET.get('pg_order_id')
    if order_id is None:
        return HttpResponseRedirect(reverse('tours:home'))
    payment_id = request.GET.get('pg_payment_id')
    salt = request.GET.get('pg_salt')
    sig = request.GET.get('pg_sig')

    application = Application.objects.filter(id=order_id).first()

    payment = Payment.objects.filter(application=application).first()
    if payment is not None:
        messages.success(request, _('Ваш билет не прошел оплату, проверьте email'))
    else:
        payment = Payment.objects.create(tour=application.tour,
                                         application=application,
                                         status=PaymentChoice.FAILURE,
                                         pg_salt=salt,
                                         pg_sig=sig,
                                         payment_id=payment_id)
        payment.save()
        messages.success(request, _('Ошибка при оплате, проверьте почту'))

    html_content = render_to_string('pages/email_failure.html', {"payment": payment})
    text_content = strip_tags(html_content)
    msg = EmailMultiAlternatives(subject=_("Ошибка при оплате билета на тур {}").format(payment.tour.city),
                                 body=text_content,
                                 from_email=settings.EMAIL_HOST_USER,
                                 to=[payment.application.email])

    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return render(request, "tour/failure.html", {"payment": payment})


def success(request, *args, **kwargs):
    order_id = request.GET.get('pg_order_id')
    if order_id is None:
        return HttpResponseRedirect(reverse('tours:home'))
    payment_id = request.GET.get('pg_payment_id')
    salt = request.GET.get('pg_salt')
    sig = request.GET.get('pg_sig')

    application = Application.objects.filter(id=order_id).first()

    payment = Payment.objects.filter(application=application).first()
    if payment is not None:
        messages.success(request, _('Ваш билет уже оплачено и отправлено в имеил'))
    else:
        payment = Payment.objects.create(tour=application.tour,
                                         application=application,
                                         status=PaymentChoice.SUCCESS,
                                         pg_salt=salt,
                                         pg_sig=sig,
                                         payment_id=payment_id)
        payment.save()
        messages.success(request, _('Успешно оплачено'))

    html_content = render_to_string('pages/email.html', {"payment": payment})
    text_content = strip_tags(html_content)
    msg = EmailMultiAlternatives(subject=_("Подтверждение билета на тур {}").format(payment.tour.city),
                                 body=text_content,
                                 from_email=settings.EMAIL_HOST_USER,
                                 to=[payment.application.email])

    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return render(request, "tour/success.html", {"payment": payment})
