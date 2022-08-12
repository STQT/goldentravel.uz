from django.urls import path
from .views import get_application

app_name = "goldentravel.applications"

urlpatterns = [
    path("<str:slug>/", get_application, name="get_application"),
]
