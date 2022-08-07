from fastapi import APIRouter
from typing import List

from models.user import User
import db

router = APIRouter()
user_db = db.db["user"]


@router.get("/users", response_description="Get all the users", response_model=List[User])
async def get_users():
    users = await user_db.find().to_list(1000)
    return users
