from aiogram import types, Dispatcher
from aiogram.filters import Command

async def start_handler(message: types.Message):
    await message.answer(f"Hello, {message.from_user.first_name}!")

def register_handlers(dp: Dispatcher):
    dp.message.register(start_handler, Command("start"))
    dp.message.register(start_handler)  # Ответ на любое сообщение