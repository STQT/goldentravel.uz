from django.contrib import admin
from django.contrib.admin import display

from .models import Application, Payment


class PaymentTabular(admin.TabularInline):
    model = Payment
    extra = 0
    readonly_fields = ("tour", "application", "status", "pg_salt", "pg_sig", "payment_id")


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ["get_tour_title", "email", "created_at", "get_payment"]
    inlines = [PaymentTabular]

    @display(ordering='tour__title', description='Тур')
    def get_tour_title(self, obj):
        return obj.tour.title

    @display(ordering='payments__created_at', description='Платежи')
    def get_payment(self, obj):
        if obj.payments.all().count() > 0:
            return True
        return False
