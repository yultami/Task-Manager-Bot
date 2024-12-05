import asyncio

from aiogram import Bot, Dispatcher
from punq import Container

from core.app.handlers.options_handlers import option_router
from core.app.handlers.start_handlers import start_router
from core.logic.container import init_container


async def main():
    container: Container = init_container()
    bot: Bot = container.resolve(Bot)
    dp: Dispatcher = container.resolve(Dispatcher)
    dp.include_routers(start_router, option_router)

    await asyncio.gather(dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types()))


if __name__ == '__main__':
    asyncio.run(main())
