import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

url = ("https://nn.cian.ru/cat.php?"
            "deal_type=sale&engine_version=2&object_type%5B0%5D=1&offer_type=flat&"
            "region=4885&room1=1&room2=1&room3=1&room4=1&room5=1&room6=1&room7=1&room9=1")

FILE_NAME = "data_flats.csv"


def get_links_flat(url_base, max_pages=54):
    href = []
    for page in range(1, max_pages+1):
        url = url_base + "&p=" + str(page)
        response = requests.get(url, allow_redirects=False)

        print("Статус получения страницы №" + str(page) + ": ", response.status_code)

        if response.status_code != 200:
            break

        contents = bs(response.text, "html.parser")

        # Отберем все объявления о продажи квартир
        apartments = contents.find_all('article')

        if len(apartments) == 0:
            print('На странице не найдены объявления!')
            break

        # Добавим ссылки на объявления в список
        for aprt in apartments:
            # Выделим ссылку из объявления
            aprt_href = aprt.find('a')['href']
            href.append(aprt_href)

    return href

href = get_links_flat(url, 100)

def get_flats(href):
    flats = []
    index = 1
    for link in href:
        dict_flat = {}
        response = requests.get(link)
        print("Статус получения квартиры №" + str(index) + ": ", response.status_code)
        index += 1

        contents = bs(response.text, "html.parser")

        type_flat = contents.find('div', class_='a10a3f92e9--container--pWxZo').text.split(',')[0]
        dict_flat['Наименование'] = type_flat

        about_flat_and_house = contents.find_all('div', class_='a10a3f92e9--item--qJhdR')
        for about in about_flat_and_house:
            field_name = about.find_all('span')[0]
            field_value = about.find_all('span')[1]
            if field_name.text not in dict_flat:
                dict_flat[field_name.text] = field_value.text

        properties = contents.find_all('div', class_='a10a3f92e9--text--eplgM')

        for property in properties:
            field_name = property.find_all('span')[0]
            field_value = property.find_all('span')[1]
            if field_name.text not in dict_flat:
                dict_flat[field_name.text] = field_value.text

        address = contents.find('address').text
        dict_flat['Адрес'] = address

        price_html = contents.find('div', class_='a10a3f92e9--amount--ON6i1')
        price = price_html.find('span').text
        dict_flat['Цена'] = price

        flats.append(dict_flat)

    return flats

flats = get_flats(href)

df = pd.DataFrame(flats)
df.to_csv(FILE_NAME)
print("Количество полученных квартир:", len(df))
print(df.head())
print(df.info())
