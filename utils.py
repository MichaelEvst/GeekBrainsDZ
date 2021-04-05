from decimal import Decimal     # Вдохновлялся разбором на вебинаре, кое-что реализовал иначе
from datetime import date
from sys import argv

import requests


def get_currency_rate(currency_code='USD'):
    currency_code = currency_code.upper()
    response_text = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    currency_starts_at_index = response_text.find(currency_code)

    if currency_starts_at_index == -1:
        return

    date_index = response_text.find('Date')
    currency_date = response_text[date_index + 6:date_index + 16]
    day_month_year = []
    for x in currency_date.split('.'):  # Заменил генератор привычным циклом
        day_month_year.append(int(x))
    refined_currency_date = date(*(reversed(day_month_year)))

    nominal = get_field('<Nominal>', response_text, currency_starts_at_index)
    currency_price = get_field('<Value>', response_text, currency_starts_at_index)
    currency_price = currency_price.replace(',', '.')

    return f'На {refined_currency_date} {nominal} {currency_code} = {Decimal(currency_price)}'


def get_field(field_name, response_text, currency_starts_at_index):
    value_start_index = response_text.find(field_name, currency_starts_at_index) + len(field_name)
    value_end_index = response_text.find('</', value_start_index)

    return response_text[value_start_index: value_end_index]


if __name__ == '__main__':
    _module_name, currence_code_arg = argv
    print(get_currency_rate(currence_code_arg))
