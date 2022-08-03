from django.shortcuts import render, redirect

from goldentravel.tours.models import Tours


def detail_view(request, *args, **kwargs):
    obj = Tours.objects.get(pk=kwargs['id'])
    return render(request, 'tour/detail.html', {"obj": obj})

