import json
from aiogram.filters import BaseFilter
from aiogram.types import Message


class Return:

    def __init__(self, path, currency) -> None:
        self.path = path
        self.currency = currency


    def create(self):
        data = json.load(open(self.path))
        anw_data = f'{self.currency}: \n Валюта: {data[self.currency][1]}\n Курс: {data[self.currency][2]}'
        return anw_data


# Check if user chose what t display
class IsCurrency(BaseFilter):

    def __init__(self) -> None:
        self.currency = json.load(open('/home/jon/PycharmProjects/Currency_bot/Parsing_data/currency_data.json'))

    async def __call__(self, msg: Message) -> bool:
        are_there = self.currency.keys()
        return msg.text in are_there
