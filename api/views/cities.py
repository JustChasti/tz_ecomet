from fastapi import APIRouter
from fastapi.responses import JSONResponse


city_router = APIRouter()


@city_router.post('/weather/{city}', response_class=JSONResponse)
async def add_city(city: str):
    print(city)
