from scrapy import Item, Field


class CityItem(Item):
    # модель для парсинга scrapy
    city_id = Field()
    temperature = Field()
    wind_speed = Field()
    pressure = Field()
