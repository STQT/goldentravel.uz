from django.urls import path
from django.views.generic import TemplateView

from goldentravel.tours.views import detail_view

app_name = "goldentravel.tours"

urlpatterns = [
    path('<int:pk>', detail_view, name='detail'),
    path("journal/", TemplateView.as_view(template_name="pages/email.html"), name="journal"),
]
