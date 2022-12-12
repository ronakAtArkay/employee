from fastapi import FastAPI

import models
from database import engin
from routers.admin.v1 import api

models.Base.metadata.create_all(bind=engin)

app = FastAPI()
app.include_router(api.router)
