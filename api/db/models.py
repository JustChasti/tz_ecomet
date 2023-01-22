from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, index=True)
    ow_id = Column(Integer)
    name = Column(String(64))


class Data(Base):
    __tablename__ = "data"
    id = Column(Integer, primary_key=True, index=True)
    city_id = Column(Integer, ForeignKey("cities.id"))
    temperature = Column(Integer)
    wind_speed = Column(Integer)
    pressure = Column(Integer)
