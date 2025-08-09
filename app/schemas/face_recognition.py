from pydantic import BaseModel

class VerifyRequest(BaseModel):
    img1: str
    img2: str

class VerifyResponse(BaseModel):
    verified: bool
    distance: float
    threshold: float
    model: str