
from telebot.types import Message

from storage import BotUserData
from api.panel import *
from bot import bot,redis_storage
from translation import translator
import utils
import config

@bot.message_handler(commands=['start', 'help'])
def send_welcome(msg:Message):
    uuid = utils.extract_uuid_from_start_command(msg.text)
    check_uuid = utils.check_uuid(uuid)
    if not check_uuid.is_valid:
        # the uuid is invalid
        #TODO: send proper message
        pass
    user_data_lang = PanelAdminAPI(uuid).me().lang if check_uuid.is_admin else PanelUserAPI(user_uuid=uuid).me().lang
    user_data = BotUserData(uuid,msg.from_user.id,msg.chat.id,user_data_lang,check_uuid.is_admin,redis_storage)
    # add user to bot redis database
    BotUserData.add()
  
    # get user information by api
    user_me = PanelUserAPI(uuid).me()
    t_values = {
        'profile_title':user_me.profile_title,
        'profile_url':user_me.profile_url,
        'brand_title':user_me.brand_title,
        'profile_usage_current':user_me.profile_usage_current,
        'profile_usage_total':user_me.profile_usage_total,
    }
    text = translator(user_data.lang,'WELCOME',t_values)
    bot.reply_to(msg,text)