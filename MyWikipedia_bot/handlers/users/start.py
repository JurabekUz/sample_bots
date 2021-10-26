from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

#Shaxsiydagi start buyrug'iga javob beruvchi handler
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\n"
                         f"Wikipeida Botiga Xush Kelibsiz! Foydalanish uchun xabar yuboring!")


