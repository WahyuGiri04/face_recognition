from pydantic import BaseModel, EmailStr, ConfigDict
import uuid

class EmployeeResponse(BaseModel):
    uuid: uuid.UUID
    full_name: str
    email: EmailStr
    image_base64: str
    
    model_config = ConfigDict(from_attributes=True)

    
    