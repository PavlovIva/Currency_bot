from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import json


kb_builder = ReplyKeyboardBuilder()
data:dict = json.load(open('/home/jon/PycharmProjects/Currency_bot/Parsing_data/currency_data.json'))
btns = [*data.keys()]

buttons = [KeyboardButton(text=item) for item in btns]
get_board = kb_builder.row(*buttons)





