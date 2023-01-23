from time import sleep

from loguru import logger

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from config import base_host, base_name, base_pass, base_port, base_user
from db.models import Base


"""
Почему postgres:
- бесплатная
- открытый исходный код
- достаточно мощная
- поддерживает много типов данных
- может обрабатывать много данных

- в целом стандартное подключение к постгресу - создание таблиц и подключение 
- делаю это через цикл, если api запустится раньше postgres, то будет реконнект
"""

connect_data = {
    'drivername': 'postgresql+psycopg2',
    'host': base_host,
    'port': base_port,
    'username': base_user,
    'password': base_pass,
    'database': base_name,
}

while True:
    try:
        engine = create_engine(URL(**connect_data))
        engine.connect()
        Base.metadata.create_all(engine)
        break
    except Exception as e:
        logger.warning('I cant connect to database. Creating her ***')
        try:
            connection = psycopg2.connect(user=base_user, password=base_pass)
            connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cursor = connection.cursor()
            cursor.execute(f"create database {base_name}")
            cursor.close()
            connection.close()
            break
        except Exception as e:
            logger.exception("Postgres connection error")
            sleep(5)

Session = sessionmaker(bind=engine)
