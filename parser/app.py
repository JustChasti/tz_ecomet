import time
from threading import Thread

import uvicorn
from fastapi import FastAPI
from loguru import logger

from config import delay, my_host
from views.weather_reguest import city_router
from source.main import get_pages


app = FastAPI()
logger.add("test.log", rotation="100 MB")


def parser():
    while True:
        start_time = time.time()
        get_pages()
        delta = time.time() - start_time
        if delta < delay:
            time.sleep(delay-delta)


@app.on_event("startup")
async def main():
    daemon = Thread(target=parser)
    daemon.start()


app.include_router(city_router)


if __name__ == "__main__":
    uvicorn.run(app, host=my_host, port=8000)
