import cv2
import numpy as np
import base64
from typing import Optional, Dict, Any
from deepface import DeepFace
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

def decode_base64_image(base64_string: str) -> Optional[np.ndarray]:
    """
    Decode base64 string to numpy array image
    """
    try:
        if not base64_string:
            logger.error("Empty base64 string provided")
            return None
            
        # Remove data URL prefix if present
        if ',' in base64_string:
            base64_string = base64_string.split(',')[1]
        
        # Validate base64 string
        if not base64_string.strip():
            logger.error("Base64 string is empty after processing")
            return None
            
        img_data = base64.b64decode(base64_string)
        
        if len(img_data) == 0:
            logger.error("Decoded image data is empty")
            return None
            
        np_arr = np.frombuffer(img_data, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        
        if img is None:
            logger.error("Failed to decode image from numpy array")
            return None
            
        logger.info("Image decoded successfully")
        return img
        
    except base64.binascii.Error as e:
        logger.error(f"Base64 decode error: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected decode error: {e}")
        return None

def verify_faces(img1: np.ndarray, img2: np.ndarray) -> Dict[str, Any]:
    """
    Verify if two face images belong to the same person
    """
    try:
        # Validate input images
        if img1 is None or img2 is None:
            raise ValueError("One or both images are None")
            
        if img1.size == 0 or img2.size == 0:
            raise ValueError("One or both images are empty")
        
        # Check if images have valid shape
        if len(img1.shape) != 3 or len(img2.shape) != 3:
            raise ValueError("Images must have 3 dimensions (height, width, channels)")
        
        logger.info("Starting face verification process")
        
        res = DeepFace.verify(
            img1, img2, 
            model_name="ArcFace",
            detector_backend="opencv",
            enforce_detection=False, 
            silent=True
        )
        
        result = {
            "verified": res["verified"], 
            "distance": res["distance"],
            "threshold": res["threshold"], 
            "model": res["model"]
        }
        
        logger.info(f"Face verification result: {result}")
        return result
        
    except ValueError as ve:
        logger.error(f"Validation error in face verification: {str(ve)}")
        raise ve
    except Exception as e:
        logger.error(f"Face verification error: {str(e)}")
        raise Exception(f"Face verification failed: {str(e)}")