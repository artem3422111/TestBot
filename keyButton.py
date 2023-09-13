from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

def one_start_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton('/Профиль')],
        [KeyboardButton('/Работа')],
        [KeyboardButton('/Forbest')],
        [KeyboardButton('/Улица')],
        [KeyboardButton('/Семья')]
    ], resize_keyboard=True)
    return kb
