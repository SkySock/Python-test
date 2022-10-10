import datetime as dt

from pydantic import BaseModel, Field
from pydantic.class_validators import List, Union

from app.city.schemas import CitySchema
from app.user.schemas import UserModel


class PicnicCreateSchema(BaseModel):
    city_id: int = Field(description='ID города, в котором проводится пикник')
    time: dt.datetime = Field(description='Дата проведения пикника')


class PicnicCreateResponseSchema(BaseModel):
    id: int
    city_name: str = Field(description='Название города')
    time: dt.datetime = Field(description='Дата пикника')

    class Config:
        orm_mode = True


class PicnicRegistrationSchema(BaseModel):
    id: int
    user: UserModel
    picnic: PicnicCreateResponseSchema

    class Config:
        orm_mode = True


class PicnicResponseSchema(BaseModel):
    id: int
    city_name: str
    time: dt.datetime
    users: List[UserModel]

    class Config:
        orm_mode = True
