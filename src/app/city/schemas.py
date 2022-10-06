from pydantic import BaseModel, Field


class CreateCity(BaseModel):
    name: str = Field(description='Название города')


class CitySchema(BaseModel):
    id: int
    name: str
    weather: float

    class Config:
        orm_mode = True
