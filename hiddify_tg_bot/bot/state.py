from telebot.handler_backends import State,StatesGroup

class UserState(StatesGroup):
    Welcome = State()
