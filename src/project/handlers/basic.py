from aiogram import Bot
from aiogram.filters import Command
from aiogram.types import Message

from src.create_bot import dp
from src.project.utils.commands import set_commands


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(836876955, text="Активация протокола")


async def stop_bot(bot: Bot):
    await bot.send_message(836876955, text="Деактивация протокола")


async def command_rules(message: Message):
    with open("group_rules.txt", "r", encoding="utf-8") as rules:
        await message.answer(rules.read())


def register_basic_handlers():
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(command_rules, Command("rules"))
