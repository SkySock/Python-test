from typing import Union
from pydantic.class_validators import List

from fastapi import APIRouter, Depends
from fastapi.params import Query
from sqlalchemy.orm import Session

from . import schemas, models
from .services import user_service
from utils import get_db_session

user_router = APIRouter()


@user_router.post('/', summary='CreateUser', response_model=schemas.UserModel)
def register_user(user: schemas.RegisterUserRequest, s: Session = Depends(get_db_session)):
    """
    Регистрация пользователя
    """
    user_object = user_service.create_user(user, s)

    return schemas.UserModel.from_orm(user_object)


@user_router.get('/', summary='Get all users', response_model=List[schemas.UserModel])
def users_list(
        min_age: Union[int, None] = Query(description='Минимальный возраст', default=None),
        max_age: Union[int, None] = Query(description='Максимальный возраст', default=None),
        s: Session = Depends(get_db_session)):
    """
    Список пользователей с фильтрацией по максимальному и минимальному возрасту
    """
    users = user_service.get_users_list(min_age, max_age, s)
    return [schemas.UserModel.from_orm(user) for user in users]
