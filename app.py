# -*- coding: cp1251 -*-
from aiogram import executor, types
from loader import dp, bot, db
import logging


async def on_startup(dp):
    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)


async def set_default_commands(dp):
    bot_commands = [
        types.BotCommand(command="start", description="Запуск бота"),
        types.BotCommand(command="sendAll", description="Отправить сообщение"),
        types.BotCommand(command="help", description="Отображает список всех доступных команд")
    ]
    await bot.set_my_commands(bot_commands)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    if message.chat.type == "group" or message.chat.type == "supergroup" or message.chat.type == "private":
        if not db.user_exists(message.from_user.id):
            db.add_user(message.from_user.id)
        await bot.send_message(message.chat.id,
                               'Привет {0.first_name} !\nЯ - Староста!\nЯ буду отправлять тебе важную информацию с ИСИТ:)'.format(
                                   message.from_user))


@dp.message_handler(commands="help")
async def command_start(message: types.Message):
    await message.answer(
        text='''
        Мои команды:
        /start - Запускает бота
        /info - Информация
        /help - Отображает список всех доступных команд
        '''
    )


@dp.message_handler(commands="sendAll")
async def sendall(message: types.Message):
    if message.chat.type == "group" or message.chat.type == "supergroup" or message.chat.type == "private":
        if message.from_user.id == 566762103:
            text = message.text[9:]
            users = db.get_user()
            for row in users:
                try:
                    if message.chat.type == "group" or message.chat.type == "supergroup":
                        await bot.send_message(row[0], "@" + message.from_user.username + ":\n " + message.text[9:])
                    if int(row[1]) != 1:
                        db.set_active(row[0], 1)
                except:
                    db.set_active(row[0], 0)

            await bot.send_message(message.from_user.id, "Успешная рассылка!")


if __name__ == '__main__':
    try:
        executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
    except (KeyboardInterrupt, SystemExit):
        logging.error("Bot stopped!")
