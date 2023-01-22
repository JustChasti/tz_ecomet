import requests
import json

from fastapi import APIRouter
from fastapi.responses import JSONResponse
from config import parser_host


city_router = APIRouter()


@city_router.post('/weather/{city}', response_class=JSONResponse)
async def add_city(city: str): # для начала пробить по базе
    data = requests.post(
        url=f'{parser_host}/city/find',
        data=json.dumps({'name': city, "ow_id": 0})
    )
    if data.status_code == 200:
        print(data.json())
        return {'info': 'succes'}
    else:
        return {'info': 'error'}
