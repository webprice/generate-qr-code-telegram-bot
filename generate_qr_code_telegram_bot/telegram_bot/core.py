import telegram
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from settings import settings

from generate_qr_code_telegram_bot.telegram_bot.handlers import handle_message, handle_start_message

bot = telegram.Bot(token=settings.TELEGRAM_BOT_TOKEN)


def run_bot():
    # Initialize the Updater with the bot token
    updater = Updater(token=settings.TELEGRAM_BOT_TOKEN, use_context=True)

    # Get the dispatcher from the updater
    dispatcher = updater.dispatcher

    # Create a command handler for the '/start' command and add it to the dispatcher
    start_handler = CommandHandler('start', handle_start_message)
    dispatcher.add_handler(start_handler)

    # Create a message handler for text messages and add it to the dispatcher
    message_handler = MessageHandler(Filters.text, handle_message)
    dispatcher.add_handler(message_handler)

    # Start polling for updates from Telegram
    updater.start_polling()

    # Idle the bot (keep it running) until manually stopped
    updater.idle()

    print("Bot stopped")
