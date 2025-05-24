from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config import Config
import logging
import asyncio
from bot.handlers.base import register_handlers

# Инициализация бота с новым синтаксисом
bot = Bot(
    token=Config.BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML) 
    )
dp = Dispatcher()

# Регистрация обработчиков
register_handlers(dp)

async def main():
    try:
        logging.basicConfig(level=logging.INFO)
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Ошибка: {e}")
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())