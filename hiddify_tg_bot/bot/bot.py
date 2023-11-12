from telebot import TeleBot
from telebot.types import Message

from api import panel
from . import utils
import config


bot = TeleBot(config.BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message:Message):
    user_uuid = utils.extract_uuid_from_start_message(message.text)
    
    api = panel.PanelAPI(user_uuid)
    u_info = api.info()

    text = f'''HI Welcome to Hiddify telegram bot :)\nYour information:\nProfile Title: {u_info.profile_title}\nProfile Url: {u_info.profile_url}\nBrand Title: {u_info.brand_title}\nCurrent Usage: {u_info.profile_usage_current}\nTotal Usage: {u_info.profile_usage_total}'''
    bot.reply_to(message,text)

def run():
    bot.infinity_polling()
