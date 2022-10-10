from fastapi import APIRouter, Query, Depends, HTTPException
from pydantic.class_validators import List
import datetime as dt

from sqlalchemy.orm import Session

from utils import get_db_session
from .schemas import PicnicCreateSchema, PicnicCreateResponseSchema, PicnicResponseSchema, PicnicRegistrationSchema
from .services import picnic_service
from ..city.services import city_service
from ..user.services import user_service

picnic_router = APIRouter()


@picnic_router.get('/', summary='All Picnics', response_model=List[PicnicResponseSchema])
def all_picnics(datetime: dt.datetime = Query(default=None, description='Время пикника (по умолчанию не задано)'),
                past: bool = Query(default=True, description='Включая уже прошедшие пикники'),
                s: Session = Depends(get_db_session)):
    """
    Список всех пикников
    """
    picnics = picnic_service.get_picnics(s, datetime, past)

    return [PicnicResponseSchema.from_orm(pic) for pic in picnics]


@picnic_router.post('/', summary='Picnic Add', response_model=PicnicCreateResponseSchema)
def picnic_add(picnic: PicnicCreateSchema,
               s: Session = Depends(get_db_session)):
    """
    Создание пикника
    """
    city = city_service.get_city_by_id(s, city_id=picnic.city_id)
    if not city:
        raise HTTPException(status_code=400, detail=f'Города с id: {picnic.city_id} не существует')

    p = picnic_service.add_picnic(s, **picnic.dict())
    return PicnicCreateResponseSchema.from_orm(p)


@picnic_router.post(
    '/{picnic_id}/users/{user_id}/',
    summary='Picnic Registration',
    response_model=PicnicRegistrationSchema
)
def register_to_picnic(picnic_id: int, user_id: int, s: Session = Depends(get_db_session)):
    """
    Регистрация пользователя на пикник
    """
    picnic = picnic_service.get_picnic_by_id(s, picnic_id)

    if not picnic:
        raise HTTPException(status_code=404, detail=f'Пикника с id: {picnic_id} не существует')

    user = user_service.get_user_by_id(s, user_id)

    if not user:
        raise HTTPException(status_code=404, detail=f'Пользователя с id: {user_id} не существует')
    if picnic.time - dt.timedelta(minutes=5) < dt.datetime.now():
        raise HTTPException(
            status_code=400,
            detail='Зарегистрироваться на пикник можно не позднее чем за 5 минут до начала'
        )

    picnic_registration = picnic_service.register_user_on_picnic(session=s, picnic_id=picnic_id, user_id=user_id)

    return PicnicRegistrationSchema.from_orm(picnic_registration)
