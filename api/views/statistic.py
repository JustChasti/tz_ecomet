from datetime import datetime
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from loguru import logger

from source.db_funcs import get_unsorted_data, get_sorted_data, find_city, get_data_period


stat_router = APIRouter()


@stat_router.get('/last_weather', response_class=JSONResponse)
async def get_last_weather(search: str=''):
    if len(search) > 0:
        if search[0] == '{':
            search = search[1:-1]
        return get_sorted_data(search)
    return get_unsorted_data()


@stat_router.get('/city_stats', response_class=JSONResponse)
async def get_last_weather(city: str='', start_date: datetime=datetime(2023, 1, 1), end_date: datetime=datetime.now()):
    if len(city) == 0 or not(find_city(city)):
        return {
            'info': 'cant find this city'
        }
    return get_data_period(city, start_date, end_date)
