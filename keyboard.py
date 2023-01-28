from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove


til = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🇺🇿 uz',callback_data='uzbek'),
            InlineKeyboardButton(text='🇺🇸 eng',callback_data='english'),
            InlineKeyboardButton(text='🇷🇺 ru',callback_data='rus')
        ],
    ]
)

menuz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='admin'),
            KeyboardButton(text="tilni o'zgartirish")
        ],
    ],
    resize_keyboard=True
)

meneng = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='admin'),
            KeyboardButton(text="change the language")
        ],
    ],
    resize_keyboard=True
)

menru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='admin'),
            KeyboardButton(text="изменить язык")
        ],
    ],
    resize_keyboard=True
)

