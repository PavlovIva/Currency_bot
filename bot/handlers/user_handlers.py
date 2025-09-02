from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from bot.Lexicon.lexica import help_info
from bot.config.user_info import user_data
from bot.Keyboards.get_board import get_board
from bot.funcs import Return, IsCurrency
from Parsing_data.parse import main, follow_favourite_currency
import json

router = Router()

# Greeting person
@router.message(Command(commands=['start']))
async def start(msg: Message) -> None:
    main()
    await msg.reply(f'Hello, {msg.from_user.username}!')
    if msg.from_user.id not in user_data:
        user_data[msg.from_user.id] = {msg.from_user.username, msg.from_user.first_name, msg.from_user.last_name, msg.from_user.is_premium}
    print(user_data)


# Give person navigation and assist
@router.message(Command(commands=['help', 'info']))
async def help_user(msg: Message) -> None:
    await msg.reply(help_info)


# Ask user what to show
@router.message(Command(commands=['get']))
async def user_choose_crn(msg: Message) -> None:
    main()
    await msg.reply("Choose", reply_markup=get_board.as_markup())


# Send user asked info
@router.message(IsCurrency())
async def send_user_info(msg: Message) -> None:
    anw_info = Return('/home/jon/PycharmProjects/Currency_bot/Parsing_data/currency_data.json', msg.text)
    await msg.reply(anw_info.create())


@router.message(Command(commands=['set']))
async def set_favorite_one(msg: Message) -> None:
    await msg.reply(follow_favourite_currency('AUD'))