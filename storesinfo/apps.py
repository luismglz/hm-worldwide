from django.apps import AppConfig
from jobs.cron import run_scheduler


class StoresinfoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'storesinfo'
    
    def ready(self) -> None:
        # run_scheduler()
        return super().ready()
        
