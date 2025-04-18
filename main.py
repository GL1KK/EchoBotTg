import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = ""

url_tg = "https://t.me/programisticDanya"
url_git = "https://github.com/GL1KK"

dp = Dispatcher()

bot = Bot(TOKEN)

logging.basicConfig(level=logging.INFO)

@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(f"Привет! Я первый эхо-бот от {url_tg}, {url_tg}. Отправь мне сообщение, а я повторю его)")
@dp.message(lambda message: message.text)
async def message_handler(message: Message):
    try:
        await message.answer(message.text)
    except Exception as e:
        await message.answer(f"Ошибка!!! {e}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())