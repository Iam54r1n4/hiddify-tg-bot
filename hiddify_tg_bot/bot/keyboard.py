from telebot import types
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

class Keyboards():
    __main_menu: InlineKeyboardMarkup = None
    def __init__(self) -> None:
        pass

    @classmethod
    def main_menu(cls):
        if cls.__main_menu:
            return cls.__main_menu
        else:

            markup = InlineKeyboardMarkup(row_width=4)

