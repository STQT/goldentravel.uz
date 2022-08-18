from ckeditor.fields import RichTextField
from django.db import models

from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class CurrencyChoice(models.IntegerChoices):
    UZS = 0, "UZS"
    USD = 1, "USD"
    EUR = 2, "EUR"


class Tours(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    short_desctions = models.CharField(max_length=200, verbose_name=_('Короткое описание'))
    description = RichTextField(_('Полное описание'))
    main_image = models.ImageField(upload_to="tours", verbose_name=_("Основное изображение"))
    city = models.CharField(max_length=100, verbose_name=_("Город"))
    amount = models.FloatField(_('Стоимость'), default=0)
    currency = models.IntegerField(_('Курс'), default=CurrencyChoice.UZS, choices=CurrencyChoice.choices)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tours:detail', args=(self.id,))

    class Meta:
        verbose_name = "Тур"
        verbose_name_plural = "Туры"


class ToursFeatures(models.Model):
    tour = models.ForeignKey(Tours, verbose_name=_("Условия тура"), on_delete=models.CASCADE, related_name="features")
    title = models.CharField(_("Название условии"), max_length=200, default="Условие")
    means = models.CharField(_("Значение"), max_length=200, default="Значение")

    def __str__(self):
        return "{} | {}".format(self.title, self.tour.city)

    class Meta:
        verbose_name = _("Условие тура")
        verbose_name_plural = _("Условии тура")


class TourBanner(models.Model):
    tour = models.ForeignKey(Tours, verbose_name=_("Баннер тура"), on_delete=models.CASCADE)
    banner_image = models.ImageField(_("Баннер"), )

    def get_absolute_url(self):
        return reverse('tours:detail', args=(self.tour.id,))

    class Meta:
        verbose_name = _("Баннер тура")
        verbose_name_plural = _("Баннеры тура")


class TourShots(models.Model):
    tour = models.ForeignKey(Tours, on_delete=models.CASCADE, related_name="shots")
    image = models.ImageField(upload_to='tourshots', verbose_name=_('Доп. изображение'))

    def __str__(self):
        return self.tour.title

    class Meta:
        verbose_name = "Изображение тура"
        verbose_name_plural = "Изображения туров"
