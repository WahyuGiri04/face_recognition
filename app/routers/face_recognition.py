from fastapi import APIRouter
from app.schemas.face_recognition import VerifyRequest, VerifyResponse
from app.schemas.base_response import BaseResponse
from app.services.face_recognition_service import decode_base64_image, verify_faces
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/face-recognition", tags=["Face Recognition"])

@router.post("/verify", response_model=BaseResponse[VerifyResponse])
async def verify_faces_endpoint(data: VerifyRequest):
    try:
        # Validate input data
        if not data.img1 or not data.img2:
            return BaseResponse.bad_request("Both img1 and img2 are required")
        
        if not data.img1.strip() or not data.img2.strip():
            return BaseResponse.bad_request("Image data cannot be empty")
        
        # Decode images
        img1 = decode_base64_image(data.img1)
        img2 = decode_base64_image(data.img2)
        
        if img1 is None:
            logger.error("Failed to decode img1")
            return BaseResponse.bad_request("Failed to decode img1. Please check the base64 format")
            
        if img2 is None:
            logger.error("Failed to decode img2")
            return BaseResponse.bad_request("Failed to decode img2. Please check the base64 format")
        
        # Verify faces
        result = verify_faces(img1, img2)
        
        logger.info("Face verification completed successfully")
        return BaseResponse.success(
            data=VerifyResponse(**result),
            message="Face verification completed successfully"
        )
        
    except ValueError as ve:
        logger.error(f"ValueError in face verification: {str(ve)}")
        return BaseResponse.bad_request(f"Invalid input data: {str(ve)}")
    
    except Exception as e:
        logger.error(f"Internal server error in face verification: {str(e)}")
        return BaseResponse.error("An unexpected error occurred during face verification")