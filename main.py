from aiogram import Bot, Dispatcher, executor, types
from config import Config
import logging
from bot.handlers.base import register_handlers

# Инициализация
bot = Bot(token=Config.BOT_TOKEN)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

# Регистрация обработчиков
register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)