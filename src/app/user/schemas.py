from pydantic import BaseModel, Field


class RegisterUserRequest(BaseModel):
    name: str = Field(description='Имя пользователя')
    surname: str = Field(description='Фамилия пользователя')
    age: int = Field(description='Возраст пользователя')


class UserModel(BaseModel):
    id: int
    name: str = Field(description='Имя пользователя')
    surname: str = Field(description='Фамилия пользователя')
    age: int = Field(description='Возраст пользователя')

    class Config:
        orm_mode = True
