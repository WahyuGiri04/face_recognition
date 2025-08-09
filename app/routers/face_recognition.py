from fastapi import APIRouter, HTTPException

from app.schemas.face_recognition import (
    VerifyRequest, VerifyResponse,
)
from app.services.face_recognition_service import (
    decode_base64_image, verify_faces
)

router = APIRouter(prefix="/face-recognition", tags=["Face Recognition"])

@router.post("/verify", response_model=VerifyResponse)
async def verify_faces_endpoint(data: VerifyRequest):
    try:
        img1 = decode_base64_image(data.img1)
        img2 = decode_base64_image(data.img2)
        
        if img1 is None or img2 is None:
            raise HTTPException(status_code=400, detail="Failed to decode one or both images")
            
        result = verify_faces(img1, img2)
        return VerifyResponse(**result)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

