# ventas/apps.py
from django.apps import AppConfig

class VentasConfig(AppConfig):
    name = 'ventas'

    def ready(self):
        import ventas.signals
