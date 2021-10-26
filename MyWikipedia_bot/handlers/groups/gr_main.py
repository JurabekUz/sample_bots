"""
 Bu faylda botimizning guruhdagi so'rovlarga javob beraadigan qismi joylashgan

"""
from aiogram import types
from aiogram.dispatcher.filters import Command
from loader import dp
import wikipedia #wikipedia paketini import qilindi
wikipedia.set_lang('uz') # foydalanish tili o'zbek tili qilib belgilandi

from filters.group_ft import IsGroup 

@dp.message_handler(IsGroup(),Command("xabar",prefixes="!/"))
async def wiki_group(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\n"
                         f"Wikipeida Boti Guruhda ishlayapti. Foydalanish uchun Reply qilib  xabar yuboring! ")
