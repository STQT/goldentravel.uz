from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from goldentravel.tours.forms import TourForm
from goldentravel.tours.models import Tours
from goldentravel.applications.models import Application


# from goldentravel.applications.models import Application


def detail_view(request, *args, **kwargs):
    if request.method == 'GET':
        obj = Tours.objects.filter(pk=kwargs['pk']).first()
        return render(request, 'tour/detail.html', {"obj": obj,
                                                    "form": TourForm(obj)})

    elif request.method == 'POST':
        obj = Tours.objects.filter(pk=kwargs['pk']).first()
        form = TourForm(obj, request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            fullname = form.cleaned_data['fullname']
            application_obj = Application.objects.create(tour=obj, email=email)
            send_mail("Qale ishlar", "MANA SHU SMS {} {}".format(fullname, application_obj), settings.EMAIL_HOST_USER,
                      [email])
            messages.success(request, _("Ваша заявка принята, в ближайшее время Вам отправят сммс по почте"))
            return redirect(reverse('tours:detail', kwargs={'pk': obj.pk}))
        else:
            return render(request, 'tour/detail.html', {"obj": obj, "form": form})


class TourFormView(DetailView):
    def post(self, request, *args, **kwargs):
        form = TourForm(request.POST or None)
        if form.is_valid():
            return redirect('/')
        return reverse('tours:detail', args=args)
