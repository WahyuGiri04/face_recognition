from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from deepface import DeepFace
import base64
import numpy as np
import cv2

app = FastAPI()

# Schema input
class ImageRequest(BaseModel):
    img1: str
    img2: str

# Decode Base64 ke OpenCV image
def decode_base64_image(base64_string: str):
    try:
        if ',' in base64_string:
            base64_string = base64_string.split(',')[1]
        image_data = base64.b64decode(base64_string)
        np_array = np.frombuffer(image_data, np.uint8)
        return cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    except Exception as e:
        print(f"Decode error: {e}")
        return None

# Endpoint verifikasi wajah
@app.post("/verify")
async def verify_faces(data: ImageRequest):
    img1 = decode_base64_image(data.img1)
    img2 = decode_base64_image(data.img2)

    if img1 is None or img2 is None:
        raise HTTPException(status_code=400, detail="Gagal decode image (img1 atau img2)")

    try:
        result = DeepFace.verify(
            img1_path=img1,
            img2_path=img2,
            model_name="ArcFace",             # <== Gunakan ArcFace
            detector_backend="opencv",        # <== Detektor ringan dan cepat
            enforce_detection=False,          # Tetap jalan meskipun wajah tidak 100% terdeteksi
            silent=True
        )

        return {
            "verified": result["verified"],
            "distance": result["distance"],
            "threshold": result["threshold"],
            "model": result["model"],
            "detector_backend": result["detector_backend"]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
