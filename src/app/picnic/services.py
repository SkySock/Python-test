from typing import Optional, List

from sqlalchemy.orm import Session
import datetime as dt

from app.picnic.models import Picnic, PicnicRegistration


class PicnicService:
    model = Picnic
    picnic_registration_model = PicnicRegistration

    def add_picnic(self, session: Session, city_id: int, time: dt.datetime) -> Picnic:
        """
        Создание пикника
        """
        picnic = self.model(city_id=city_id, time=time)
        session.add(picnic)
        session.commit()

        return picnic

    def get_picnics(self, session: Session, datetime: dt.datetime, past: bool) -> List[Picnic]:
        """
        Возвращает пикники удовлетворяющие условию
        """
        picnics = session.query(self.model)
        if datetime is not None:
            picnics = picnics.filter(self.model.time == datetime)
        if not past:
            picnics = picnics.filter(self.model.time >= dt.datetime.now())

        return picnics

    def get_picnic_by_id(self, session: Session, picnic_id: int) -> Optional[Picnic]:
        """
        Получение пикника по id.
        """
        return session.query(self.model).get(picnic_id)

    def register_user_on_picnic(self, session: Session, picnic_id: int, user_id: int) -> PicnicRegistration:
        """
        Регистрирует пользователя на пикник, если пользователь еще не зарегистрирован
        """
        picnic_registration = session.query(self.picnic_registration_model).filter(
            self.picnic_registration_model.user_id == user_id,
            self.picnic_registration_model.picnic_id == picnic_id).first()

        if picnic_registration:
            return picnic_registration

        picnic_registration = self.picnic_registration_model(picnic_id=picnic_id, user_id=user_id)
        session.add(picnic_registration)
        session.commit()

        return picnic_registration


picnic_service = PicnicService()
