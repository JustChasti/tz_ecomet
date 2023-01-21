from fastapi import APIRouter
from fastapi.responses import JSONResponse
from views.models import CityModel
from db.connection import Session


city_router = APIRouter()


@city_router.post('/city/find', response_class=JSONResponse)
async def find_city(city: CityModel):

    return {
        'info': f'city {city.name} exist',
        'name': city.name,
        'ow_id': city.ow_id
    }
