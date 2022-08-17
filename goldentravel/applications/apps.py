from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ApplicationsConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'goldentravel.applications'
    verbose_name = _("Заявки")

    def ready(self):
        try:
            import goldentravel.users.signals  # noqa F401
        except ImportError:
            pass
