from django.shortcuts import render


def get_application(request, slug):
    return render(request, 'test.html', {'slug': slug})
