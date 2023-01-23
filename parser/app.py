import time
from threading import Thread

import uvicorn
from fastapi import FastAPI
from loguru import logger

from config import delay, my_host
from views.weather_reguest import city_router
from source.main import get_pages
from urllib3.exceptions import MaxRetryError


app = FastAPI()
logger.add("test.log", rotation="100 MB")


def parser():
    while True:
        try:
            start_time = time.time()
            get_pages()
            delta = time.time() - start_time
            if delta < delay:
                time.sleep(delay-delta)
        except MaxRetryError as e:
            logger.warning(e)
            time.sleep(5)


@app.on_event("startup")
async def main():
    # при запуске приложения стартует фоновый поток для ежеминутной обработки данных
    daemon = Thread(target=parser)
    daemon.start()


app.include_router(city_router)


if __name__ == "__main__":
    uvicorn.run(app, host=my_host, port=5000)
