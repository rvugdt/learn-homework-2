"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

from datetime import datetime, timedelta

def print_days():
    today = datetime.now()
    yesterday = datetime.now() - timedelta(days=1)
    month_ago = datetime.now() - timedelta(days=30)
    print(f'Вчера: {yesterday.strftime("%Y-%m-%d")}')
    print(f'Сегодня: {today.strftime("%Y-%m-%d")}')
    print(f'30 дней назад: {month_ago.strftime("%Y-%m-%d")}')

def str_2_datetime(date_string):
    date_and_time = datetime.strptime(date_string, "%m/%d/%y %H:%M:%S.%f")
    return date_and_time

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
