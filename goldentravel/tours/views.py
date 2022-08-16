from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.html import strip_tags
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from goldentravel.tours.forms import TourForm
from goldentravel.tours.models import Tours
from goldentravel.applications.models import Application

from django.template.loader import render_to_string
from goldentravel.utils.init_payment import send_request


def send_mail_converter(values: dict) -> str:
    html_content = render_to_string('pages/email.html', values)
    text_content = strip_tags(html_content)
    return text_content


def detail_view(request, *args, **kwargs):
    if request.method == 'GET':
        obj = Tours.objects.filter(pk=kwargs['pk']).first()
        pg_sig = send_request(obj.id, obj.amount, obj.title)
        return render(request, 'tour/detail.html', {"obj": obj,
                                                    "form": TourForm(obj),
                                                    "pg_sig": pg_sig})

    elif request.method == 'POST':
        obj = Tours.objects.filter(pk=kwargs['pk']).first()
        form = TourForm(obj, request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            fullname = form.cleaned_data['fullname']
            application_obj = Application.objects.create(tour=obj, email=email)
            html_content = render_to_string('pages/email.html', {"fullname": fullname, "tour": obj,
                                                                 "app": application_obj})
            text_content = strip_tags(html_content)
            msg = EmailMultiAlternatives(subject=_("Подтверждение билета на тур {}").format(obj.city),
                                         body=text_content,
                                         from_email=settings.EMAIL_HOST_USER,
                                         to=[email])

            msg.attach_alternative(html_content, "text/html")
            msg.send()
            # send_mail(_("Подтверждение билета на тур {}").format(obj.city),
            #           "MANA SHU SMS {} {}".format(fullname, application_obj), settings.EMAIL_HOST_USER,
            #           [email])
            messages.success(request, _("Ваша заявка принята, в ближайшее время Вам отправят сммс по почте"))
            return redirect(reverse('tours:detail', kwargs={'pk': obj.pk}))
        else:
            return render(request, 'tour/detail.html', {"obj": obj, "form": form})


def result(request):
    print(request)
    return 200


def check(request):
    print(request)
    return 200
