import asyncio
import logging
from os import getenv

from handlers.register import register_router
from handlers.shop import shop_router

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


TOKEN = "8125936730:AAGrr5KjzSrZ92nX-8xhjemZ9tVeYWQt4_M"

async def main() -> None:
    dp = Dispatcher()
    dp.include_routers(
        register_router,
        shop_router,
    )

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
