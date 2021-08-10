from django.apps import AppConfig


class MQTTConfig(AppConfig):
    name = 'mqtt'

    def ready(self):
        from .client import client
        client.loop_start()