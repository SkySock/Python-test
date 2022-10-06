from fastapi import APIRouter

from app.city.routers import city_router
from app.user.routers import user_router
from app.picnic.routers import picnic_router

api_router = APIRouter()

api_router.include_router(user_router, prefix='/users', tags=['users'])
api_router.include_router(city_router, prefix='/cities', tags=['cities'])
api_router.include_router(picnic_router, prefix='/picnics', tags=['picnics'])
