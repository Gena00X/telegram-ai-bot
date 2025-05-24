from aiogram import types, Dispatcher
from aiogram.filters import Command
import logging
from config import Config
async def start_handler(message: types.Message):
    if Config.LOG_MESSAGES=="true":
        logging.info(f"Получено сообщение от {message.from_user.full_name} (ID: {message.from_user.id}): {message.text}")
    await message.answer(f"Hello, {message.from_user.first_name}!")

def register_handlers(dp: Dispatcher):
    dp.message.register(start_handler, Command("start"))
    dp.message.register(start_handler)  # Ответ на любое сообщение