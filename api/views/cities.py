import requests
import json

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from config import parser_host
from source.db_funcs import find_city, add_city_to_db


city_router = APIRouter()


@city_router.post('/weather/{city}', response_class=JSONResponse)
async def add_city(city: str):
    if find_city(city):
        return {
            'info': 'city already exist',
            'city': {'name': city}
        }
    data = requests.post(
        url=f'{parser_host}/city/find',
        data=json.dumps({'name': city, "ow_id": 0})
    )
    if data.status_code == 200:
        add_city_to_db(data.json()['name'], data.json()['ow_id'])
        return {
            'info': 'New city added to base',
            'city': {
                'name': city, 
                'openweather_id': data.json()['ow_id']
            }
        }
    else:
        return {
            'info': "Can't find this city on openweathermap.org",
            'city': {'name': city}
        }
