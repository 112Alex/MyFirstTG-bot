import asyncio
import logging
import env

from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
from aiogram.filters import CommandStart, Command


bot = Bot(token=env.BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.reply(text=f'Hello, {message.from_user.full_name}')

@dp.message(Command("help"))
async def handle_help(message: types.Message):
    text = "I'm an echo bot.\nSend me any message!"
    await message.answer(text=text)

@dp.message()
async def echo_message(message: types.Message):
    # if message.text.startswith("/start"):
    await message.send_copy(chat_id=message.chat.id)
    if message.text:
        await message.reply(text=message.text)
    elif message.sticker:
        await message.reply_sticker(sticker=message.sticker.file_id)
    # elif message.photo:
    #     await message.reply_photo()
    else:
        await message.reply(text="Something new...")
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())