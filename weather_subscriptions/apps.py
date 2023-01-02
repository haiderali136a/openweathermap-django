from django.apps import AppConfig


class WeatherSubscriptionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'weather_subscriptions'

    def ready(self):
        from weather_check import weather_updater
        weather_updater.start()
