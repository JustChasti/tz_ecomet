from fastapi import APIRouter
from fastapi.responses import JSONResponse
from views.models import CityModel
from db.connection import Session


# по сути только 1 вью для поиска города, решил внести его парсер,
# чтобы не переносить дополнительные модули в api

city_router = APIRouter()


@city_router.post('/city/find', response_class=JSONResponse)
async def find_city(city: CityModel):
    # вью для поиска города, поиск происходит при валидации модели
    return {
        'info': f'city {city.name} exist',
        'name': city.name,
        'ow_id': city.ow_id
    }
