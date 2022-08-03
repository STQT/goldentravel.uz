from django.urls import path

from goldentravel.tours.views import detail_view


app_name = "goldentravel.tours"
urlpatterns = [
    path('<int:id>', detail_view, name='detail'),

]
