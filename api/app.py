import uvicorn
from fastapi import FastAPI
from loguru import logger

from config import my_host
from views.cities import city_router
from views.statistic import stat_router


app = FastAPI()
app.include_router(city_router)
app.include_router(stat_router)


if __name__ == "__main__":
    uvicorn.run(app, host=my_host, port=8000)
