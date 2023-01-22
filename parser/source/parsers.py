import os

from scrapy import Selector
from loguru import logger

from source.items import CityItem
from source.selenium_request import get_city_html
from db.models import Data
from db.connection import Session
from config import test_mode
from decorators import default_decorator


@default_decorator('error in geting page and parsing items')
async def get_item(db_id, ow_id):
    city = CityItem()
    get_city_html(db_id, ow_id)
    html_file = f"temp/{db_id}.html"
    with open(html_file, 'r', encoding='utf-8-sig', newline='') as f:
        page = f.read()
        data = Selector(text=str(page))
        city['city_id'] = db_id
        city['temperature'] = data.css('span.heading::text').get()
        city['wind_speed'] = data.css('div.wind-line::text').get()
        elements = data.css('ul.weather-items ::text').extract()
        city['pressure'] = elements[1]
    os.remove(html_file)
    insert_data(city)


@default_decorator('error in insertion items')
def insert_data(city: CityItem):
    session = Session()
    data = Data(
        city_id=city['city_id'],
        temperature=int(city['temperature'].split('°')[0]),
        wind_speed=float(city['wind_speed'].split('m/s')[0]),
        pressure=int(city['pressure'].split('h')[0])
    )
    session.add(data)
    session.commit()
    session.close()
    if test_mode:
        logger.info(f"City {city['city_id']} data updated")


# @default_decorator('error in finding city')
def add_city(name):
    html_file = f'temp/find_{name}.html'
    city = {
        'name': name,
        'id': 0
    }
    with open(html_file, 'r', encoding='utf-8-sig', newline='') as f:
        page = f.read()
        data = Selector(text=str(page))
        table = data.css('.table')
        if not table:
            city['id'] = 0
        else:
            cities = table.css('a')
            if not cities:
                city['id'] = 0
            else:
                city['id'] = cities[0].attrib['href'].split('/city/')[1]
        if test_mode:
            logger.info(f'City {name} - {city["id"]}')
    os.remove(html_file)
    return city
