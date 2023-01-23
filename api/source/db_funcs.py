from db.connection import Session
from db.models import City, Data
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


def get_unsorted_data():
    session = Session()
    data = []
    for i in session.query(City).all():
        city = i.__dict__
        obj = session.query(Data).filter_by(city_id=city['id']).order_by(Data.id.desc()).first()
        obj = obj.__dict__
        logger.info(obj)
        data.append({
            'city': city['name'],
            'data':{
                'temperature': obj['temperature'],
                'wind_speed': obj['wind_speed'],
                'pressure': obj['pressure']
            }
        })
    return data


def get_sorted_data(name):
    name = name.capitalize()
    session = Session()
    data = []
    cities = [i.__dict__ for i in session.query(City).all()]
    matched = []
    for index, item in list(enumerate(cities)):
        if item['name'] == name:
            matched.append(item)
            cities.remove(item)
            break
    for j in range(len(name)):
        for index, item in list(enumerate(cities)):
            if item['name'] in name[:len(name)-j] or name[:len(name)-j] in item['name']:
                matched.append(item)
                cities.remove(item)
    matched.extend(cities)

    for i in matched:
        obj = session.query(Data).filter_by(city_id=i['id']).order_by(Data.id.desc()).first()
        obj = obj.__dict__
        data.append({
            'city': i['name'],
            'data':{
                'temperature': obj['temperature'],
                'wind_speed': obj['wind_speed'],
                'pressure': obj['pressure']
            }
        })
    return data
