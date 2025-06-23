import os
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import Update
# from .models import TelegramUser
from django.utils import timezone
from django.apps import apps

load_dotenv()
bot_token = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    TelegramUser = apps.get_model('bot_setup.TelegramUser')  # Access the model dynamically
    user_name = update.message.from_user.username
    if user_name:
        user_name = f"@{user_name}"
    else:
        user_name = update.message.from_user.full_name or "unknown user" # Fallback if no username
    chat_creation_timestamp = update.message.date
    chat_creation_timestamp = timezone.make_aware(chat_creation_timestamp)
    
    TelegramUser.objects.create(
        user_name=user_name,
        chat_creation_timestamp=chat_creation_timestamp
    )
    



    await update.message.reply_text(
        """
        Hello! Let's explore the world of Khanha Lal! \n/help -> list of all available commands
        """
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
        /start -> Lets start fresh \n/info -> About Khanha Lal \n/website -> The first video from Python playlist \n/contact -> contact info
        """
    )

async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
        I am a freelance developer specializing in Telegram bot development, automation, and full-stack web applications. I've worked with 40+ global clients via Fiverr and Upwork, delivering custom solutions in Python, Flutter, and React. My work includes anonymous chatbots, Google Maps data scrapers, Discord bots, and SaaS platforms. With a 5.0-star rating and a reputation for timely, high-quality delivery, I bring strong technical skills and client-focused solutions.
        """
    )

async def website(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Check out my work at https://www.fiverr.com/bohraa")

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("You will be connecting with our agent in a few minutes...")

def main():
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(bot_token).build()

    # Register your command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command)) # Renamed to avoid conflict with built-in help
    application.add_handler(CommandHandler("info", info))
    application.add_handler(CommandHandler("website", website))
    application.add_handler(CommandHandler("contact", contact))

    print("Bot started, start interacting at @Little983_bot")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()