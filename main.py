import requests
from bs4 import BeautifulSoup

def digs_to_months(x):
    if x < 1 or x > 12:
        return 'error'
    if x == 1:
        return 'января'
    if x == 2:
        return 'февраля'
    if x == 3:
        return 'марта'
    if x == 4:
        return 'апреля'
    if x == 5:
        return 'мая'
    if x == 6:
        return 'июня'
    if x == 7:
        return 'июля'
    if x == 8:
        return 'августа'
    if x == 9:
        return 'сентября'
    if x == 10:
        return 'октября'
    if x == 11:
        return 'ноября'
    if x == 12:
        return 'декабря'


while True:
    try:
        print('Введите адрес YouTube-ролика:')
        url = input()

        bs = BeautifulSoup(requests.get(url).text, "lxml")
        date = bs.find("meta", itemprop="uploadDate").get("content")
        full_date = date.split('-')
        month = digs_to_months(int(full_date[1]))

        print(f'Видеоролик было выложен: {full_date[2]} {month} {full_date[0]}', end='\n\n')

    except Exception as e:
        print(e)
