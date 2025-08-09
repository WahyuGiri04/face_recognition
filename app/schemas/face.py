from pydantic import BaseModel
from typing import Optional
import uuid
from datetime import datetime

class FaceBase(BaseModel):
    employee_id: int
    image_base64: str
    is_active: Optional[bool] = True
    is_deleted: Optional[bool] = False

class FaceCreate(FaceBase):
    pass

class FaceUpdate(BaseModel):
    image_base64: Optional[str] = None
    is_active: Optional[bool] = None
    is_deleted: Optional[bool] = None

class FaceResponse(FaceBase):
    id: int
    uuid: uuid.UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
