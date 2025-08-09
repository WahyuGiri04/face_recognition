from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
import uuid
from datetime import datetime

class EmployeeBase(BaseModel):
    full_name: str
    email: EmailStr
    is_active: Optional[bool] = True
    is_deleted: Optional[bool] = False

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None
    is_deleted: Optional[bool] = None

class EmployeeResponse(EmployeeBase):
    id: int
    uuid: uuid.UUID
    created_at: datetime
    updated_at: datetime
    
    model_config = ConfigDict(from_attributes=True)