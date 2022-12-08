from fastapi import FastAPI
from app.routers import base

app = FastAPI()

app.include_router(base.router)
