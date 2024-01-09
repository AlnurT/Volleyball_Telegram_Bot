import asyncio
import logging
import sys

from src.create_bot import bot, dp
from src.project.handlers import basic, other


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s",
        stream=sys.stdout,
    )
    basic.register_basic_handlers()
    other.register_other_handlers()

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
