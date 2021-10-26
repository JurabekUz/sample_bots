"""
    Bu faylda botning asosiy qismi joylashgan
    Shaxsiydagi so'rovlarga javob beradigan qismi joylashgan
"""
from aiogram import types

from loader import dp
import wikipedia #wikipedia paketini import qilindi
wikipedia.set_lang('uz') # foydalanish tili o'zbek tili qilib belgilandi


@dp.message_handler(state=None)
async def wiki_private(message: types.Message):
    try: # malumot topishga haraqat qilamiz
        respond = wikipedia.summary(message.text)
        await message.answer(respond) #,aqola topilsa javob
    except: # agarda xatolik yuz bersa,malumot topilmasa shu qism ishga tushadi
        await message.answer("Uzr. Bu mavzuga oid malumot topilmadi")







