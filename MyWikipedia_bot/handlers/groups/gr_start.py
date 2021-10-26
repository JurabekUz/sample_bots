"""
Foydalanuvchi guruhda start komandasini yuborganida
Salom, .......
Wikipedia Boti Guruhda ishlayapti. Foydalanish uchun Reply qilib xabar  yuboring 
yoki /xabar buyrug'i orqali menga murojat qilishingiz mumkin! 

"""

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from filters.group_ft import IsGroup # IsGroup filteri import qilingan 
from loader import dp

#gruhdagi start komandasiga javob beruvchi handler
@dp.message_handler(CommandStart(),IsGroup())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\n"
                         f"Wikipeida Boti Guruhda ishlayapti. Foydalanish uchun Reply qilib yuboring. \n"
                         f"/xabar buyrug'i  orqali menga murojat qilishingiz mumkin! ")
