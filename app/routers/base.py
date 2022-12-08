from fastapi import APIRouter
from app.models.base import HelloIn, HelloOut

router = APIRouter()

@router.post("/", response_model=HelloOut ,tags=["root"])
async def root(msg: HelloIn):
    return {"msg": f"Hello World {msg.msg}"}
