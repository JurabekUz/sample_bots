from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"<b>Assalomu alaykum</b> \n       Bu bot orqali siz   \n "
    "<b>Sonlarni Rim va Arab raqamlarida ifodalashingiz mumkin!</b>\n"
    "<b>Matnlarni katta va kichik harflarda ifodalashingiz mumkin</b>")
