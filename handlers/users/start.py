from aiogram import types
from loader import dp


@dp.message_handler(commands='start')
async def start(message: types.Message):
    if message.chat.type == "group" or message.chat.type == "supergroup" or message.chat.type == "private":
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id)
        await bot.send_message(message.chat.id,
                               'Привет {0.first_name} !\nЯ - Староста!\nЯ буду отправлять тебе важную информацию с ИСИТ:)'.format(
                                   message.from_user))
