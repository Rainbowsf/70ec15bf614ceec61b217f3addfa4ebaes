from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'


class MainAppConfig(AppConfig):
    name = "main"
    verbose_name = "Приложение с графиками"  # Делаем русское имя нашему приложению
