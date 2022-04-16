from fastapi import APIRouter, Body, Depends, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from app.startMessage import service

router = APIRouter()

@router.get("/make-team")
async def hi():
    return {"Hello": "World"}
