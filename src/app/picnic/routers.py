from fastapi import APIRouter, Query, Depends
import datetime as dt

from sqlalchemy.orm import Session

from utils import get_db_session
from .models import PicnicRegistration, Picnic
from .services import picnic_service
from ..city.models import City

picnic_router = APIRouter()


@picnic_router.get('/', summary='All Picnics')
def all_picnics(datetime: dt.datetime = Query(default=None, description='Время пикника (по умолчанию не задано)'),
                past: bool = Query(default=True, description='Включая уже прошедшие пикники'),
                s: Session = Depends(get_db_session)):
    """
    Список всех пикников
    """
    picnics = picnic_service.get_picnics(s, datetime, past)

    return [{
        'id': pic.id,
        'city': s.query(City).filter(City.id == pic.id).first().name,
        'time': pic.time,
        'users': [
            {
                'id': pr.user.id,
                'name': pr.user.name,
                'surname': pr.user.surname,
                'age': pr.user.age,
            }
            for pr in s.query(PicnicRegistration).filter(PicnicRegistration.picnic_id == pic.id)],
    } for pic in picnics]


@picnic_router.post('/', summary='Picnic Add')
def picnic_add(city_id: int = None, datetime: dt.datetime = None,
               s: Session = Depends(get_db_session)):
    p = Picnic(city_id=city_id, time=datetime)
    s.add(p)
    s.commit()

    return {
        'id': p.id,
        'city': Session().query(City).filter(City.id == p.id).first().name,
        'time': p.time,
    }


@picnic_router.post('/{picnic_id}/users/{user_id}/', summary='Picnic Registration')
def register_to_picnic(s: Session = Depends(get_db_session), *_, **__, ):
    """
    Регистрация пользователя на пикник
    (Этот эндпойнт необходимо реализовать в процессе выполнения тестового задания)
    """
    # TODO: Сделать логику
    return ...
