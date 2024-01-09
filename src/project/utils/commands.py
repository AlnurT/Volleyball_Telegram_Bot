from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="rules", description="Правила группы"),
        BotCommand(command="poll", description="Создать опрос"),
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
