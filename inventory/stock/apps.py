from django.apps import AppConfig


class StockConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "inventory.stock"
    
    def ready(self):
        from . import signals