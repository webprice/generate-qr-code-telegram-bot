from dotenv import load_dotenv
import os

load_dotenv()


class Settings():
    TELEGRAM_BOT_TOKEN: str =  os.environ.get("TELEGRAM_BOT_TOKEN")
    GITHUB_REPO_URL: str = os.environ.get("GITHUB_REPO_URL")
    OWNER_TELEGRAM_ID: str = os.environ.get("OWNER_TELEGRAM_ID") if os.environ.get("OWNER_TELEGRAM_ID") else None
    OWNER_WEBSITE_URL: str = os.environ.get("OWNER_WEBSITE_URL") if os.environ.get("OWNER_WEBSITE_URL") else "https://hrekov.com/"
    QR_TEXT_LENGTH: int = int(os.environ.get("QR_TEXT_LENGTH")) if os.environ.get("QR_TEXT_LENGTH") else 256
    QR_IMAGE_BOX_SIZE: int = int(os.environ.get("QR_IMAGE_BOX_SIZE")) if os.environ.get("QR_IMAGE_BOX_SIZE") else 512
    TELEGRAM_BOT_URL: str = os.environ.get("TELEGRAM_BOT_NAME") if os.environ.get("TELEGRAM_BOT_NAME") else "https://t.me/responseWithQrBot"
    APP_PORT: int = int(os.environ.get("APP_PORT")) if os.environ.get("APP_PORT") else 8000

settings = Settings()


