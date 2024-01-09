from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

from src.create_bot import dp


async def command_start(message: Message):
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


async def command_rules(message: Message):
    with open("group_rules.txt", "r", encoding="utf-8") as rules:
        await message.answer(rules.read())


def register_basic_handlers():
    dp.message.register(command_start, CommandStart())
    dp.message.register(command_rules, Command("rules"))
