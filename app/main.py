from fastapi import FastAPI
from app.api.routers import openweather_router

app = FastAPI()

app.include_router(openweather_router)
