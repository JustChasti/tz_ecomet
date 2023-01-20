from fastapi import APIRouter
from fastapi.responses import JSONResponse
from views.models import AddCityModel


city_router = APIRouter()


@city_router.post('/city/add', response_class=JSONResponse)
async def add_city(playlist: AddCityModel):
    # добавление города в базу
    return {'info': 'city added'}
