from telebot import TeleBot
from .storage import HiddifyStateRedisStorage
import config

from telebot.types import Message

from .storage import BotUserData
from api.panel import *
from .translation import translator
import hiddify_tg_bot.bot.utils as utils
import config


REDIS_STORAGE = HiddifyStateRedisStorage(redis_url=config.REDIS_URI)

BOT = TeleBot(config.BOT_TOKEN,state_storage=REDIS_STORAGE)



@BOT.message_handler(commands=['start'])
def send_welcome(msg:Message):
    uuid = utils.extract_uuid_from_start_command(msg.text)
    check_uuid = utils.check_uuid(uuid)
    if not check_uuid.is_valid:
        # the uuid is invalid
        #TODO: send proper message
        pass
        return
    # get user information by "me/" api 
    me_data = PanelAdminAPI(uuid).me() if check_uuid.is_admin else PanelUserAPI(uuid).me()
    user_data = BotUserData(uuid,msg.from_user.id,msg.chat.id,me_data.lang,check_uuid.is_admin,REDIS_STORAGE)
    # add user to bot redis database
    user_data.add()
  
    # get user information by api
    t_values = {
        'profile_title':me_data.profile_title,
        'profile_url':me_data.profile_url,
        'brand_title':me_data.brand_title,
        'profile_usage_current':me_data.profile_usage_current,
        'profile_usage_total':me_data.profile_usage_total,
    }
    text = translator(user_data.lang,'messages.welcome',t_values)
    BOT.reply_to(msg,text)



def run():
    BOT.infinity_polling()