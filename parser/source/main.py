from db.connection import Session
from db.models import City
from source.parsers import get_item
from loguru import logger
import asyncio


def get_pages():
    session = Session()
    cities = session.query(City).all()
    for i in cities:
        asyncio.run(get_item(int(i.id), int(i.ow_id)))
    session.close()
