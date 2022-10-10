import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создание сессии
POSTGRES_DB = os.environ.get('POSTGRES_DB', default='postgres')
POSTGRES_USER = os.environ.get('POSTGRES_USER', default='postgres')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST', default='127.0.0.1')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT', default='5432')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', default='postgres')

SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Подключение базы (с автоматической генерацией моделей)
Base = declarative_base()
