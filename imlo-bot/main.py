import logging

from aiogram import Bot, Dispatcher, executor, types
from checkword import check_word

API_TOKEN = '1743215209:AAF0OGW7O-qZNiFzT7_vEsf_eNczXtenrXg'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    await message.reply(" Ajoyib imlo botga xush kelibsiz")

@dp.message_handler(commands='help')
async def send_welcome(message: types.Message):
    await message.reply("Sizga qanday yordam kerak\n botda foydalanish uchun so'z yuboring")

    """
    This handler will be called when user sends `/start` or `/help` command
    """


@dp.message_handler()
async def checkImlo(xabar: types.Message):
    word=xabar.text
    result=check_word(word)
    if result['available']:
        response=f" to'g'ri: {word.capitalize()}\n"
    else:
        response=f" xato: {word.capitalize}\n"
        for text in result['matches']:
            response+=f"to'g'ri: {text.capitalize()}"
    await xabar.answer(response)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

