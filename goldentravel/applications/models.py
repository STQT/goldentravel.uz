import uuid

from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from goldentravel.tours.models import Tours
from django.conf import settings


class Application(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    url = models.URLField()
    fullname = models.CharField(max_length=255, blank=True, verbose_name=_('Полное имя пользователя'))
    pay_url = models.URLField(verbose_name=_("Ссылка на оплату"))
    email = models.EmailField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tour = models.ForeignKey(Tours, on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse('applications:get_application', args=(self.pk,))

    def save(self, *args, **kwargs):
        self.url = settings.SITE_URL + self.get_absolute_url()
        super().save(*args, **kwargs)

    def __str__(self):
        return "{} {}".format(self.tour.title, self.email)

    class Meta:
        ordering = ('created_at',)
        verbose_name = _("Заявка")
        verbose_name_plural = _("Заявки")


class Checkout(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.application.email

    class Meta:
        ordering = ('application',)


class PaymentChoice(models.IntegerChoices):
    SUCCESS = 0, _("УСПЕШНО")
    FAILURE = 1, _("ОШИБКА")


class Payment(models.Model):
    tour = models.ForeignKey(Tours, on_delete=models.CASCADE)
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='payments')
    payment_id = models.CharField(max_length=100, blank=True)
    pg_salt = models.CharField(max_length=255, verbose_name=_('Ключевое слово'))
    pg_sig = models.CharField(max_length=255, verbose_name=_('Подпись'))
    status = models.IntegerField(verbose_name=_('Статус'), default=0,
                                 choices=PaymentChoice.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Платеж')
        verbose_name_plural = _('Платежи')

    def __str__(self):
        return "{} | {}".format(self.application.fullname, self.application.email)
