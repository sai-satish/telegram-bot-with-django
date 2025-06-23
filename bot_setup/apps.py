# telegram_bot/apps.py
from django.apps import AppConfig
from .tasks import start_bot

class TelegramBotConfig(AppConfig):
    name = 'telegram_bot'

    def ready(self):
        # Start the bot via Celery task
        start_bot.apply_async()
