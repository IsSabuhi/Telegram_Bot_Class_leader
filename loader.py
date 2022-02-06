from aiogram import Bot, Dispatcher, types
import logging
from data import config
from db import Database


# Configure logging
logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

db = Database("database.db")


