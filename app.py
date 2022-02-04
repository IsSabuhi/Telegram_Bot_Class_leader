from aiogram import executor
from loader import dp


async def on_startup(dp):

    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)



    from utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)

    print("Бот запущен")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
