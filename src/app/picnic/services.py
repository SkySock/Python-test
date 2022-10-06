from sqlalchemy.orm import Session
import datetime as dt

from app.picnic.models import Picnic, PicnicRegistration


class PicnicService:
    model = Picnic
    picnic_registration_model = PicnicRegistration

    def get_picnics(self, session: Session, datetime, past):
        picnics = session.query(self.model)
        if datetime is not None:
            picnics = picnics.filter(self.model.time == datetime)
        if not past:
            picnics = picnics.filter(self.model.time >= dt.datetime.now())

        return picnics


picnic_service = PicnicService()
