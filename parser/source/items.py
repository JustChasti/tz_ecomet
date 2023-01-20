from scrapy import Item, Field


class CityItem(Item):
    city_id = Field()
    temperature = Field()
    wind_speed = Field()
    pressure = Field()
