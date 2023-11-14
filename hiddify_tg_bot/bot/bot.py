from telebot import TeleBot
from storage import HiddifyStateRedisStorage

import config

redis_storage = HiddifyStateRedisStorage(config.REDIS_URI)

bot = TeleBot(config.BOT_TOKEN,state_storage=redis_storage)

def run():
    bot.infinity_polling()
