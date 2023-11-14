from collections import namedtuple


NAME = "hiddify_tg_bot"

Check_UUID_Tuple = namedtuple('CheckUUIDResult','is_valid, is_admin')
UserID_ChatID_Tuple = namedtuple('UserId_ChatId','user_id, chat_id')