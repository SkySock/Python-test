from sqlalchemy.orm import Session
from typing import Optional, List

from ..user import schemas
from .models import User


class UserService:
    model = User

    def create_user(self, session: Session, user: schemas.RegisterUserRequest) -> User:
        user_obj = self.model(**user.dict())
        session.add(user_obj)
        session.commit()
        return user_obj

    def get_user_by_id(self, session: Session, user_id: int) -> Optional[User]:
        return session.query(self.model).get(user_id)

    def get_users_list(self, session: Session, min_age: int, max_age: int) -> List[User]:
        users = session.query(self.model)
        if min_age:
            users = users.filter(self.model.age >= min_age)
        if max_age:
            users = users.filter(self.model.age <= max_age)

        return users


user_service = UserService()
