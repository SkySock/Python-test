from sqlalchemy.orm import Session

from app.city.models import City


class CityService:
    model = City

    def create_city(self, city_name: str, session: Session):
        city_object = session.query(self.model).filter(self.model.name == city_name.capitalize()).first()
        if city_object is None:
            city_object = self.model(name=city_name.capitalize())
            session.add(city_object)
            session.commit()
        return city_object

    def get_cities_list(self, session: Session):
        return session.query(self.model).all()


city_service = CityService()
