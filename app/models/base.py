from fastapi import FastAPI
from pydantic import BaseModel

class HelloIn(BaseModel):
    msg: str

class HelloOut(BaseModel):
    msg: str