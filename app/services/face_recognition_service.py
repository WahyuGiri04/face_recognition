import cv2
import numpy as np
import base64
from typing import Optional, Dict, Any
from deepface import DeepFace

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

def decode_base64_image(base64_string: str) -> Optional[np.ndarray]:
    try:
        if ',' in base64_string:
            base64_string = base64_string.split(',')[1]
        img_data = base64.b64decode(base64_string)
        np_arr = np.frombuffer(img_data, np.uint8)
        return cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    except Exception as e:
        print("Decode error:", e)
        return None

def verify_faces(img1: np.ndarray, img2: np.ndarray) -> Dict[str, Any]:
    try:
        res = DeepFace.verify(
            img1, img2, 
            model_name="ArcFace",
            detector_backend="opencv",
            enforce_detection=False, 
            silent=True
        )
        return {
            "verified": res["verified"], 
            "distance": res["distance"],
            "threshold": res["threshold"], 
            "model": res["model"]
        }
    except Exception as e:
        raise Exception(f"Face verification error: {str(e)}")