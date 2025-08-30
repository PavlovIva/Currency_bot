from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from bot.Lexicon.lexica import help_info
from bot.config.user_info import user_data

router = Router()

# Greeting person
@router.message(Command(commands=['start']))
async def start(msg: Message) -> None:
    await msg.reply(f'Hello, {msg.from_user.username}!')
    if msg.from_user.id not in user_data:
        user_data[msg.from_user.id] = {msg.from_user.username, msg.from_user.first_name, msg.from_user.last_name, msg.from_user.is_premium}
    print(user_data)


# Give person navigation and assist
@router.message(Command(commands=['help', 'info']))
async def help_user(msg: Message) -> None:
    await msg.reply(help_info)