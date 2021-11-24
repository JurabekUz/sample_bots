from aiogram import types
from utils.funcsion import Solution,intToRoman
from loader import dp

@dp.message_handler()
async def exchange(message: types.Message):
    rim_raqamlar=['I','V','X',"L",'C','D','M']
    xabar=message.text
    son_rim=list(xabar)
    if xabar.isdigit():
        son=int(xabar)
        respond=intToRoman(son)
        await message.answer(f"Javob: {respond}")
        
    elif all(item in rim_raqamlar for item in son_rim):
        obj=Solution()
        respond=obj.romanToInt(xabar)
        await message.answer(f"Javob: {respond}")
    else:
        await message.reply(xabar.upper())
        await message.reply(xabar.lower())
