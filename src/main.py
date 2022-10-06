from fastapi import FastAPI
from app import routers
from app.user import models as user_models
from app.city import models as city_models
from app.picnic import models as picnic_models
from database import Session, engine

user_models.Base.metadata.create_all(bind=engine)
city_models.Base.metadata.create_all(bind=engine)
picnic_models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(routers.api_router, prefix='/api/v1')
