import json
import requests
import schedule, time
from bs4 import BeautifulSoup as bs

base_url = 'https://www.cbr.ru/currency_base/daily/'

response = requests.get(base_url)
# Parse data from website and save it in dictionary.
def get_all_currency() -> dict:
    currency_data = {}
    soup = bs(response.text, 'lxml')
    row_currency_table = soup.find('table', class_='data').find_all('tr')
    currency_table = [item.text.split('\n')[1:-1] for item in row_currency_table[1:]]
    for currency in currency_table:
        currency_data[currency[1]] = [currency[2], currency[3], currency[4] ]
    return currency_data


# Start main logic and save data in json.file
def main():
    if response.status_code == 200:
        currency_data = get_all_currency()
        with open('currency_data.json', 'w', encoding='utf-8') as f:
            json.dump(currency_data, f, ensure_ascii=False, indent=4)


# Get info only about favorite ones regularly
def follow_favourite_currency():
    pass
# Schedule library - TODO
"""
schedule.every(1).minutes.do(main)
while True:
    schedule.run_pending()
    time.sleep(1)"""


