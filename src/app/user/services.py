from sqlalchemy.orm import Session

from ..user import schemas
from .models import User


class UserService:
    model = User

    def create_user(self, user: schemas.RegisterUserRequest, session: Session) -> User:
        user_obj = self.model(**user.dict())
        session.add(user_obj)
        session.commit()
        return user_obj

    def get_users_list(self, min_age, max_age, session: Session):
        users = session.query(self.model)
        if min_age:
            users = users.filter(self.model.age >= min_age)
        if max_age:
            users = users.filter(self.model.age <= max_age)

        return users.all()


user_service = UserService()
