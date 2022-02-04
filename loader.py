from aiogram import Bot, Dispatcher, types
import logging
from data import config

# Configure logging
logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
# CHAT_ID = config.CHAT_ID
# db = Database("database.db")
#
#
# async def setup_bot_commands(dp):
#     bot_commands = [
#         types.BotCommand(command="start", description="Запустить бота"),
#         types.BotCommand(command="sendAll", description="Отправить сообщение")
#     ]
#     await bot.set_my_commands(bot_commands)
#
#
# @dp.message_handler(commands='start')
# async def start(message: types.Message):
#     if message.chat.type == "group" or message.chat.type == "supergroup" or message.chat.type == "private":
#         if not db.user_exists(message.from_user.id):
#             db.add_user(message.from_user.id)
#         await bot.send_message(message.chat.id,
#                                'Привет {0.first_name} !\nЯ - Староста!\nЯ буду отправлять тебе важную информацию с ИСИТ:)'.format(
#                                    message.from_user))
#
#
# @dp.message_handler(commands=['sendAll'])
# async def sendall(message: types.Message):
#     if message.chat.type == "group" or message.chat.type == "supergroup" or message.chat.type == "private":
#         if message.from_user.id == 566762103:
#             text = message.text[9:]
#             users = db.get_user()
#             for row in users:
#                 try:
#                     if message.chat.type == "group" or message.chat.type == "supergroup":
#                         await bot.send_message(row[0], "@" + message.from_user.username + ":\n " + message.text[9:])
#                     if int(row[1]) != 1:
#                         db.set_active(row[0], 1)
#                 except:
#                     db.set_active(row[0], 0)
#
#             await bot.send_message(message.from_user.id, "Успешная рассылка!")
