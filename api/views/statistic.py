from fastapi import APIRouter
from fastapi.responses import JSONResponse
from loguru import logger

from source.db_funcs import get_unsorted_data, get_sorted_data


stat_router = APIRouter()


@stat_router.get('/last_weather', response_class=JSONResponse)
async def get_last_weather(search: str=''):
    if len(search) > 0:
        if search[0] == '{':
            search = search[1:-1]
        return get_sorted_data(search)
    return get_unsorted_data()