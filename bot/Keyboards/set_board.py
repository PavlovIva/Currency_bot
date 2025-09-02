from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardBuilder
import json


kb_builder = InlineKeyboardBuilder()
data:dict = json.load(open('/home/jon/PycharmProjects/Currency_bot/Parsing_data/currency_data.json'))
btns = [*data.keys()]


buttons = [InlineKeyboardButton(text=item, callback_data=item) for item in btns]
set_board = kb_builder.row(*buttons).as_markup()



