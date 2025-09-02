import json, os
import requests
import schedule, time
from bs4 import BeautifulSoup as bs

base_url = 'https://www.cbr.ru/currency_base/daily/'


# Parse data from website and save it in dictionary.
def get_all_currency() -> dict:
    response = requests.get(base_url)
    currency_data = {}
    soup = bs(response.text, 'lxml')
    row_currency_table = soup.find('table', class_='data').find_all('tr')
    currency_table = [item.text.split('\n')[1:-1] for item in row_currency_table[1:]]
    for currency in currency_table:
        currency_data[currency[1]] = [currency[2], currency[3], currency[4] ]
    return currency_data


# Start main logic and save data in json.file
def main():
        currency_data = get_all_currency()
        if os.getcwd() == 'Parsing_data':
            with open('currency_data.json', 'w', encoding='utf-8') as f:
                json.dump(currency_data, f, ensure_ascii=False, indent=4)
        else:
            os.chdir('/home/jon/PycharmProjects/Currency_bot/Parsing_data')
            with open('currency_data.json', 'w', encoding='utf-8') as f:
                json.dump(currency_data, f, ensure_ascii=False, indent=4)


# Get info only about favorite ones regularly
def follow_favourite_currency(crns):
    response = requests.get(base_url)
    fav_soup = bs(response.text, 'lxml')
    fav_crns = [item.text.split('\n')[1:-1] for item in fav_soup.find('table', class_='data').find_all('tr')[1:]]
    for crn in fav_crns:
        if crns in crn:
            anw = f'{crn[1]}: \n Валюта: {crn[3]} \n Курс: {crn[4]}'
            return anw




# Schedule library - TODO
"""
schedule.every(1).minutes.do(main)
while True:
    schedule.run_pending()
    time.sleep(1)"""


