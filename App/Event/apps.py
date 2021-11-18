from django.apps import AppConfig

class EventConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'App.Event'

    def ready(self):
        from . import signals
