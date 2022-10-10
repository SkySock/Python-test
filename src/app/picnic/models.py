from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.city.models import City
from database import Base, Session


class Picnic(Base):
    """
    Пикник
    """
    __tablename__ = 'picnic'

    id = Column(Integer, primary_key=True, autoincrement=True)
    city_id = Column(Integer, ForeignKey('city.id'), nullable=False)
    time = Column(DateTime, nullable=False)

    @property
    def city_name(self) -> str:
        s = Session()
        return s.query(City).filter(City.id == self.city_id).first().name

    @property
    def users(self):
        return [user_reg.user for user_reg in self.user_registrations]

    def __repr__(self):
        return f'<Пикник {self.id}>'


class PicnicRegistration(Base):
    """
    Регистрация пользователя на пикник
    """
    __tablename__ = 'picnic_registration'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    picnic_id = Column(Integer, ForeignKey('picnic.id'), nullable=False)

    user = relationship('User', backref='picnics')
    picnic = relationship('Picnic', backref='user_registrations')

    def __repr__(self):
        return f'<Регистрация {self.id}>'
