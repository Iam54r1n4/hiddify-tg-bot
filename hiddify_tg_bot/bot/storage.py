from hiddify_tg_bot.bot.state import StateRedisStorage
import config

class HiddifyStateRedisStorage(StateRedisStorage):
    def __init__(self, host='localhost', port=6379, db=0, password=None, prefix='telebot_', redis_url=None):
        super().__init__(host, port, db, password, prefix, redis_url)

    def get_user_lang(self,user_id,chat_id):
        self.get_data(chat_id,user_id)['lang']
        

Redis_Storage = HiddifyStateRedisStorage(config.REDIS_URI)

class BotUserData():
    def __init__(self,uuid,user_id,chat_id,lang,is_admin,storage:HiddifyStateRedisStorage) -> None:
        self.__storage = storage
        self.uuid = uuid
        self.user_id = user_id
        self.chat_id = chat_id
        self.lang = lang
        self.is_admin = is_admin
    
    # add user data to storage
    def add(self):
        # get instance variables
        variables = [var_name for var_name in self.__dict__.keys() if not var_name.startswith('__')]
        for var_name in variables:
            self.__storage.set_data(self.chat_id,self.user_id,var_name,self.var)
    # remove user data from storage
    def remove(self):
        self.__storage.reset_data(self.chat_id,self.user_id)
    # update user data from storage
    def update(self):
        self.add()
    @staticmethod
    def from_storage(storage:HiddifyStateRedisStorage,user_id,chat_id):
        return BotUserData(storage.get_data(chat_id,user_id)['uuid'],user_id,chat_id,storage.get_data(chat_id,user_id)['lang'],storage)