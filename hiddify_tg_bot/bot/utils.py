from api.panel import PanelAPI
from base import *
from telebot.types import Message

def extract_uuid_from_start_command(start_msg:str):
    pruned = start_msg.split(' ')[1].strip()
    if pruned.startswith('admin_'):
        return pruned.removeprefix('admin_')
    else:
        return pruned

def check_uuid(uuid) -> Check_UUID_Tuple:
    api = PanelAPI(uuid,uuid)
    admin = api.admin_me()
    if admin:
        return Check_UUID_Tuple(True,True)
    else:
        user = api.user_me()
        if user:
            return Check_UUID_Tuple(True,False)
        
    return Check_UUID_Tuple(False,False)

def get_userid_chatid(msg:Message):
    return UserID_ChatID_Tuple(user_id=msg.from_user.id,chat_id=msg.chat.id)