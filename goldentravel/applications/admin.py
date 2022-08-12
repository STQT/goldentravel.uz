from django.contrib import admin
from django.contrib.admin import display

from .models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ["get_tour_title", "email"]

    @display(ordering='tour__title', description='Тур')
    def get_tour_title(self, obj):
        return obj.tour.title
