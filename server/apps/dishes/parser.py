import csv
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def get_all_dishes_from_menu(html):
    soup = BeautifulSoup(html, "html.parser")
    # парсим информацию о блюдах с главной страницы
    all_dish = soup.find('div', class_='pins__content').findAll('article')
    static_url = 'https://mikeandmollycafe.ru/static/'
    for dish in all_dish:
        price = dish.get('data-price')
        name = dish.get('data-title')
        url_image_big = f'{static_url}{dish.get("data-image_big")}'
        url_image = f'{static_url}{dish.get("data-image")}'
        category = dish.get('data-category')
        description = dish.get('data-text')
        weight = dish.get('data-weight')
        with open('./csv/dishes.csv', 'a', encoding='utf-8') as output:
            writer = csv.writer(output)
            row = (name, price, url_image_big, url_image,
                   category, description, weight)
            writer.writerow(row)

    # парсим ссылки изображений со слайдера главной страницы
    promo = soup.find('div', class_='js_slides').findAll('a')
    for element in promo:
        image = f'{static_url}{(element.get("style"))[30:-2]}'
        name = urlparse(image).path.split('/')[-1]
        with open('./csv/promo.csv', 'a', encoding='utf-8') as output:
            writer = csv.writer(output)
            row = (name, image)
            writer.writerow(row)


def main():
    url = 'https://mikeandmollycafe.ru/'
    html = get_html(url)
    get_all_dishes_from_menu(html)


if __name__ == '__main__':
    main()
