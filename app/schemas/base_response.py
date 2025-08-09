from pydantic import BaseModel
from typing import Optional, Any, Generic, TypeVar

T = TypeVar('T')

class BaseResponse(BaseModel, Generic[T]):
    status_code: int
    message: str
    data: Optional[T] = None
    
    @classmethod
    def success(cls, data: T = None, message: str = "Success", status_code: int = 200):
        return cls(
            status_code=status_code,
            message=message,
            data=data
        )
    
    @classmethod
    def error(cls, message: str = "Internal Server Error", status_code: int = 500):
        return cls(
            status_code=status_code,
            message=message,
            data=None
        )
    
    @classmethod
    def not_found(cls, message: str = "Data not found"):
        return cls(
            status_code=404,
            message=message,
            data=None
        )
    
    @classmethod
    def bad_request(cls, message: str = "Bad request"):
        return cls(
            status_code=400,
            message=message,
            data=None
        )