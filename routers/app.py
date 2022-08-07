from fastapi import APIRouter
from typing import List

from models.app import App
import db

router = APIRouter()
app_db = db.db["app"]


@router.get("/apps", response_description="Get all the apps", response_model=List[App])
async def get_apps():
    apps = await app_db.find().to_list(1000)
    return apps
