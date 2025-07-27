# backend/main.py
import os
import uuid
import json
import cv2
import numpy as np
import base64
from fastapi import FastAPI, HTTPException, UploadFile, File, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from deepface import DeepFace

# ---------- FASTAPI SETUP ----------
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------- MODEL ----------
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# ---------- UTIL ----------
def decode_base64_image(base64_string: str):
    try:
        if ',' in base64_string:
            base64_string = base64_string.split(',')[1]
        img_data = base64.b64decode(base64_string)
        np_arr = np.frombuffer(img_data, np.uint8)
        return cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    except Exception as e:
        print("Decode error:", e)
        return None

# ---------- SCHEMA ----------
class ImageRequest(BaseModel):
    img1: str
    img2: str

class PersonRecord(BaseModel):
    user_id: str
    name: str
    image: str

class LoadDbRequest(BaseModel):
    data: List[PersonRecord]

class IdentifyRequest(BaseModel):
    img: str

# ---------- ENDPOINT DETEKSI ----------
@app.post("/detect")
async def detect_faces(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    if img is None:
        raise HTTPException(400, "Decode error")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    return {"faces": [{"x": int(x), "y": int(y), "w": int(w), "h": int(h)} for x, y, w, h in faces]}

# ---------- ENDPOINT VERIFY ----------
@app.post("/verify")
async def verify_faces(data: ImageRequest):
    img1 = decode_base64_image(data.img1)
    img2 = decode_base64_image(data.img2)
    if img1 is None or img2 is None:
        raise HTTPException(400, "Decode error")
    try:
        res = DeepFace.verify(img1, img2, model_name="ArcFace",
                              detector_backend="opencv",
                              enforce_detection=False, silent=True)
        return {"verified": res["verified"], "distance": res["distance"],
                "threshold": res["threshold"], "model": res["model"]}
    except Exception as e:
        raise HTTPException(500, str(e))

# ---------- ENDPOINT LOAD DATABASE ----------
import shutil
@app.post("/load_db")
async def load_database(payload: LoadDbRequest):
    db_root = "faces"
    if os.path.exists(db_root):
        shutil.rmtree(db_root)
    os.makedirs(db_root, exist_ok=True)

    for p in payload.data:
        folder = os.path.join(db_root, p.name)
        os.makedirs(folder, exist_ok=True)
        img = decode_base64_image(p.image)
        if img is None:
            continue
        file_name = f"{p.user_id}_{uuid.uuid4().hex}.jpg"
        cv2.imwrite(os.path.join(folder, file_name), img)

    return {"status": "ok", "count": len(payload.data)}

# ---------- ENDPOINT IDENTIFY ----------
@app.post("/identify")
async def identify_face(data: IdentifyRequest):
    img = decode_base64_image(data.img)
    if img is None:
        raise HTTPException(400, "Decode error")
    try:
        dfs = DeepFace.find(img, db_path="faces", model_name="ArcFace",
                            detector_backend="opencv",
                            enforce_detection=False, silent=True)
        if dfs and not dfs[0].empty:
            best = dfs[0].iloc[0]
            identity = os.path.basename(os.path.dirname(best["identity"]))
            distance = float(best["ArcFace_cosine"])
            return {"name": identity, "distance": distance}
    except Exception as e:
        raise HTTPException(500, str(e))
    return {"name": "unknown"}

# ---------- WEBSOCKET REALTIME IDENTIFY ----------
@app.websocket("/ws/stream_identify")
async def ws_stream(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_text()
            img = decode_base64_image(data)
            if img is None:
                await websocket.send_text(json.dumps({"name": "unknown"}))
                continue
            dfs = DeepFace.find(img, db_path="faces", model_name="ArcFace",
                                detector_backend="opencv",
                                enforce_detection=False, silent=True)
            if dfs and not dfs[0].empty:
                best = dfs[0].iloc[0]
                identity = os.path.basename(os.path.dirname(best["identity"]))
                distance = float(best["ArcFace_cosine"])
                await websocket.send_text(json.dumps({"name": identity, "distance": distance}))
            else:
                await websocket.send_text(json.dumps({"name": "unknown"}))
    except WebSocketDisconnect:
        pass