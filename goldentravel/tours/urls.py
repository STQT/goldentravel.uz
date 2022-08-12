from django.urls import path

from goldentravel.tours.views import detail_view, TourFormView

app_name = "goldentravel.tours"
urlpatterns = [
    path('<int:pk>', detail_view, name='detail'),
    path('send_mail/', TourFormView.as_view(), name='send_mail'),
]
