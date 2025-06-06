import os
from dotenv import load_dotenv
import logging
load_dotenv()

class Config:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    ADMIN_ID = int(os.getenv("ADMIN_ID", 0))
    LOG_MESSAGES = os.getenv("LOG_MESSAGES", "false")