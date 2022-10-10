from typing import Optional, List

from sqlalchemy.orm import Session

from app.city.models import City


class CityService:
    model = City

    def create_city(self, session: Session, city_name: str) -> City:
        city_object = session.query(self.model).filter(self.model.name == city_name.capitalize()).first()
        if city_object is None:
            city_object = self.model(name=city_name.capitalize())
            session.add(city_object)
            session.commit()
        return city_object

    def get_city_by_id(self, session: Session, city_id: int) -> Optional[City]:
        return session.query(self.model).get(city_id)

    def get_cities_list(self, session: Session, q: str = None) -> List[City]:
        cities = session.query(self.model)
        if q:
            cities = cities.filter(self.model.name.ilike('%' + q + '%'))
        return cities


city_service = CityService()
