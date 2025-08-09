from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.schemas.face import FaceCreate, FaceUpdate, FaceResponse
from app.services.face_service import (
    create_face, get_all_faces, get_face_by_id,
    update_face, delete_face
)

router = APIRouter(prefix="/faces", tags=["Faces"])

@router.post("/", response_model=FaceResponse)
def create_face_endpoint(face: FaceCreate, db: Session = Depends(get_db)):
    return create_face(db, face)

@router.get("/", response_model=List[FaceResponse])
def get_faces(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_all_faces(db, skip, limit)

@router.get("/{face_id}", response_model=FaceResponse)
def get_face(face_id: int, db: Session = Depends(get_db)):
    db_face = get_face_by_id(db, face_id)
    if not db_face:
        raise HTTPException(status_code=404, detail="Face not found")
    return db_face

@router.put("/{face_id}", response_model=FaceResponse)
def update_face_endpoint(face_id: int, face: FaceUpdate, db: Session = Depends(get_db)):
    updated_face = update_face(db, face_id, face)
    if not updated_face:
        raise HTTPException(status_code=404, detail="Face not found")
    return updated_face

@router.delete("/{face_id}")
def delete_face_endpoint(face_id: int, db: Session = Depends(get_db)):
    deleted_face = delete_face(db, face_id)
    if not deleted_face:
        raise HTTPException(status_code=404, detail="Face not found")
    return {"detail": "Face deleted successfully"}