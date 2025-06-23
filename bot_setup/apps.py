# telegram_bot/apps.py
from django.apps import AppConfig
from .tasks import start_bot

class TelegramBotConfig(AppConfig):
    name = 'bot_setup'

    def ready(self):
        # Start the bot via Celery task
        start_bot.apply_async()
