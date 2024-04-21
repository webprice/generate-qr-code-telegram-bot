
import uvicorn
import logging
from settings import settings

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
def app():
    from generate_qr_code_telegram_bot.telegram_bot.core import run_bot
    print(f"Starting {settings.TELEGRAM_BOT_URL} Telegram bot")
    run_bot()



if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info",reload=True)
