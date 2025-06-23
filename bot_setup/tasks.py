# telegram_bot/tasks.py
from celery import shared_task
from .bot import main  # Assuming the `run_bot` function is in your bot.py

@shared_task
def start_bot():
    main()
