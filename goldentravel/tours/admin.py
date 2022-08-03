from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Tours, TourShots, TourBanner


class TourShotsInline(admin.TabularInline):
    model = TourShots
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = "Изображение"


class TourBannerInline(admin.TabularInline):
    model = TourBanner
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.banner_image.url} width="100" height="110"')

    get_image.short_description = "Изображение"


@admin.register(Tours)
class TourAdmin(admin.ModelAdmin):
    inlines = [TourShotsInline, TourBannerInline]


@admin.register(TourShots)
class TourShotsAdmin(admin.ModelAdmin):
    pass
