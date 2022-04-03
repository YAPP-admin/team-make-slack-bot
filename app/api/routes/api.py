from fastapi import APIRouter, Body, Depends, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from app.services import service

router = APIRouter()

@router.get("/")
async def hi():
    return {"Hello": "World"}
