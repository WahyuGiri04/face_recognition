from pydantic import BaseModel, EmailStr
from typing import List
import uuid

class FaceResponse(BaseModel):
    uuid: uuid.UUID
    image_base64: str

    class Config:
        orm_mode = True

class EmployeeResponse(BaseModel):
    uuid: uuid.UUID
    full_name: str
    email: EmailStr
    faces: List[FaceResponse] = []

    class Config:
        orm_mode = True