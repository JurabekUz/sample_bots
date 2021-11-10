from aiogram import types
from googletrans import Translator
from loader import dp
translator=Translator()

# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    matn=message.text
    lang=translator.detect(matn).lang
    dest='uz' if lang=='en' else 'en'
    try:
        tarjima=translator.translate(matn,dest).text
        await message.reply(tarjima)
    except:
        await message.reply("Uzr qandaydir xatolik yuz berdi")
    



