from aiogram import types, Dispatcher

async def hello_handler(message: types.Message):
    await message.answer(f"Hello, {message.from_user.first_name}!")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(hello_handler)