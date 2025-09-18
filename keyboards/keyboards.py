from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
button_1 = KeyboardButton(text='Товар 1')
button_2 = KeyboardButton(text='Товар 2')
button_3 = KeyboardButton(text='Товар 3')
button_4 = KeyboardButton(text='Товар 4')
keyboard_tov_1 = ReplyKeyboardMarkup(
    keyboard=[[button_1]], resize_keyboard=True
)
keyboard_tov_2 = ReplyKeyboardMarkup(
    keyboard=[[button_1],[button_2]], resize_keyboard=True
)
keyboard_tov_3 = ReplyKeyboardMarkup(
    keyboard=[[button_1],[button_2],[button_3]], resize_keyboard=True
)
keyboard_tov_4 = ReplyKeyboardMarkup(
    keyboard=[[button_1],[button_2],[button_3],[button_4]], resize_keyboard=True
)
