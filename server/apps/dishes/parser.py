import csv

import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def get_all_dishes_from_menu(html):
    soup = BeautifulSoup(html, "html.parser")
    all_dish = soup.find('div', class_='pins__content').findAll('article')
    for dish in all_dish:
        price = dish.get('data-price')
        name = dish.get('data-title')
        url_image_big = f'https://mikeandmollycafe.ru/static/{dish.get("data-image_big")}'
        url_image = f'https://mikeandmollycafe.ru/static/{dish.get("data-image")}'
        category = dish.get('data-category')
        description = dish.get('data-text')
        weight = dish.get('data-weight')
        with open('./csv/dishes.csv', 'a', encoding='utf-8') as output:
            writer = csv.writer(output)
            row = (name, price, url_image_big, url_image, category, description, weight)
            writer.writerow(row)


def main():
    url = 'https://mikeandmollycafe.ru/'
    html = get_html(url)
    get_all_dishes_from_menu(html)


if __name__ == '__main__':
    main()
