from fastapi import Query, HTTPException, Depends, APIRouter, Body
from sqlalchemy.orm import Session
from pydantic.class_validators import List

from app.city import services
from app.city.schemas import CreateCity, CitySchema
from external_requests import CheckCityExisting
from utils import get_db_session

city_router = APIRouter()


@city_router.post('/', summary='Create City', description='Создание города по его названию', response_model=CitySchema)
def create_city(
        city: CreateCity,
        s: Session = Depends(get_db_session)):
    if city.name is None:
        raise HTTPException(status_code=400, detail='Параметр city должен быть указан')
    check = CheckCityExisting()
    if not check.check_existing(city.name):
        raise HTTPException(status_code=400, detail='Параметр city должен быть существующим городом')

    city_object = services.city_service.create_city(city.name, s)

    return CitySchema.from_orm(city_object)


@city_router.get('/', summary='Get Cities', response_model=List[CitySchema])
def cities_list(q: str = Query(description="Название города", default=None), s: Session = Depends(get_db_session)):
    """
    Получение списка городов
    """
    cities = services.city_service.get_cities_list(s)

    return [CitySchema.from_orm(city) for city in cities]
