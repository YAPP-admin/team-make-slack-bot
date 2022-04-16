from fastapi import APIRouter, Body, Depends, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from app.services.startMessage import startMessage
from app.services.makeTeamMessage import makeTeamMessage

router = APIRouter()

@router.get("/make-team/start")
def startMessageController():
    startMessage()

@router.get("/make-team/end")
def makeTeamMessageController():
    makeTeamMessage()
