from fastapi import APIRouter
from fastapi.responses import JSONResponse


city_router = APIRouter()
CityModel = None


@city_router.post('/city/add', response_class=JSONResponse)
async def add_city(playlist: CityModel):
    # весь парсинг в том числе и проверку существования города перенес сюда
    return {'info': 'city added'}
