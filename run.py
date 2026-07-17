import asyncio

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.client.session.aiohttp import AiohttpSession

from config import TOKEN

session = AiohttpSession(proxy="http://127.0.0.1:10809")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(massage: Message):
    await massage.answer("Привет!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())