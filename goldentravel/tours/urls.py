from django.urls import path
from django.views.generic import TemplateView

from goldentravel.tours.views import detail_view, success, failure

app_name = "goldentravel.tours"

urlpatterns = [
    path('tours/<int:pk>', detail_view, name='detail'),
    path("failure/", failure, name='check'),
    path("success/", success, name='success'),
    path("journal/", TemplateView.as_view(template_name="pages/email.html"), name="journal"),
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
]
