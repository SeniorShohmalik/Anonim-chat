from cgitb import text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
natija = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Xa✅"),KeyboardButton(text="Yo\'q❌")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    )
menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Do`stimga yozish✍️"),KeyboardButton(text="Qoidalar va maslahatlar📄")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    )