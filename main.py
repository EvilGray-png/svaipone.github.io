import asyncio
import logging

from bot.handlers import commands, callbacks_handlers
from bot.texts.texts import PREVIEW
from misc import bot, dispatcher as dp


async def main() -> None:
    dp.include_routers(
        commands.router,
        callbacks_handlers.router,
    )

    try:
        await dp.start_polling(bot)
    except Exception as _ex:
        print(f'There is an exception - {_ex}')


if __name__ == "__main__":
    print(PREVIEW)
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
