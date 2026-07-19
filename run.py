import asyncio
import logging

from aiogram import Bot, Dispatcher,F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(massage: Message):
    await massage.answer("Привет!")

@dp.message(Command("help"))
async def get_help(massange:Message):
    await massange.answer("Привет этот бот пока ничего не умеет((")

@dp.message(F.text == "Как у Ивана дела?")
async def how_are_ivan(massange: Message):
    await massange.answer("У Ивана все прекрасно")

@dp.message(F.photo)
async def get_photo(massange:Message):
    await massange.answer(f"ID фото: {massange.photo[-1].file_id}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")

