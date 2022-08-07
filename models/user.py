from pydantic import EmailStr, BaseModel
from .utils import PyObjectId


class User(BaseModel):
    id: PyObjectId
    name: str = None
    email: EmailStr
    password: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

