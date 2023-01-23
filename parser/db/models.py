import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    # Модель для города
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, index=True)
    ow_id = Column(Integer)
    name = String(length=64)


class Data(Base):
    # Модель для статистики
    __tablename__ = "data"
    id = Column(Integer, primary_key=True, index=True)
    city_id = Column(Integer, ForeignKey("cities.id"))
    temperature = Column(Integer)
    wind_speed = Column(Integer)
    pressure = Column(Integer)
    created_date = Column(DateTime, default=datetime.datetime.now())
