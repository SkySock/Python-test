from pydantic import BaseModel, Field


class CreateCity(BaseModel):
    name: str = Field(description='Название города')


class CitySchema(BaseModel):
    id: int
    name: str = Field(description='Название города')
    weather: float = Field(description='Температура воздуха')

    class Config:
        orm_mode = True
