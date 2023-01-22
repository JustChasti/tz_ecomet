from pydantic import BaseModel, validator, constr
from loguru import logger

from source.selenium_request import find_city
from source.parsers import add_city

from config import test_mode


class CityModel(BaseModel):
    name: constr(max_length=64)
    ow_id = 0

    @validator('ow_id')
    def check_exist(cls, ow_id, values):
        if test_mode:
            logger.info('check existintg')
        find_city(values['name'])
        city = add_city(values['name'])
        if city['id'] == 0:
            raise ValueError(f'city {values["name"]} not found')
        ow_id = city['id']
        return ow_id
