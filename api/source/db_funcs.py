from db.connection import Session
from db.models import City
from loguru import logger


def find_city(name:str) -> bool:
    session = Session()
    city = session.query(City).filter_by(name=name).all()
    session.close()
    logger.info(city)
    if city:
        return True
    else:
        return False


def add_city_to_db(name, ow_id):
    session = Session()
    city = City(
        name=name,
        ow_id=ow_id
    )
    session.add(city)
    session.commit()
    session.close()
