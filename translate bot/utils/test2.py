'''from aiogram import types
from loader import dp
import os
from datetime import datetime
from utils.set_bot_commands import set_default_commands
from text_to_speech import speak

dt = datetime.now().strftime("%d%m%Y%H%M%S")


@dp.message_handler()
async def text_sp(msg:types.Message):
    path = f"C:\\Users\\users\\acer\\myjob\\botproject\\translate bot\\data"
    file_name = f"{path}\\speech{dt}.mp3"
    speak(msg.text, "en", save=True, file=file_name)



    await msg.answer_audio(file_name)

    #await msg.reply_audio(speak(msg.text, "en", save=True, file="Hello-World.mp3"))'''