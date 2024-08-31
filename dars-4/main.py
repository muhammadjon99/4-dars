from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
from obhavo import obhavomalumoti

telegramapi = '7476335138:AAFXpdjSWXPyHlFof5OeOf3Jpqiu6lUOqPM'
bot = Bot(telegramapi)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: Message):
    chatid = message.chat.id
    await bot.send_message(chatid, text='Xush kelibsiz. Shahar nomini kiritng')



@dp.message_handler()
async def getshahar(message: Message):
    chatid = message.chat.id
    shahar = message.text
    data = obhavomalumoti(shahar)
    if data == 'Shaxar topilmadi':
        await bot.send_message(chat_id=chatid, text=data)
    else:
        icon = f"https://openweathermap.org/img/wn/{data[1]}@4x.png"
        await bot.send_photo(chat_id=chatid, caption=data[0], photo=icon)



executor.start_polling(dp, skip_updates=True)