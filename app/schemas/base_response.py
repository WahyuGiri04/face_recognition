from typing import Generic, TypeVar
from pydantic import BaseModel

T = TypeVar('T')

class BaseResponse(Generic[T], BaseModel):
    message: str
    status_code: int
    data: T | None = None