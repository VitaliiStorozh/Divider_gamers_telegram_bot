from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


"""Use standard keyboard with two upper keys and one down key"""

menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Registration"),
            KeyboardButton(text="Start"),

        ],
        [
            KeyboardButton(text="Clear player list")
        ]
    ],
    resize_keyboard=True
)