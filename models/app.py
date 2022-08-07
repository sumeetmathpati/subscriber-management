from pydantic import BaseModel, Field
from bson import ObjectId

from .utils import PyObjectId

class App(BaseModel):
    id: PyObjectId = Field(alias="_id")
    name: str = None

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
