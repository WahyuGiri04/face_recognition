from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app import schemas, services

router = APIRouter(prefix="/faces", tags=["Faces"])

@router.post("/", response_model=schemas.face.FaceResponse)
def create_face(face: schemas.face.FaceCreate, db: Session = Depends(get_db)):
    return services.face_service.create_face(db, face)

@router.get("/", response_model=List[schemas.face.FaceResponse])
def get_faces(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return services.face_service.get_all_faces(db, skip, limit)

@router.get("/{face_id}", response_model=schemas.face.FaceResponse)
def get_face(face_id: int, db: Session = Depends(get_db)):
    db_face = services.face_service.get_face_by_id(db, face_id)
    if not db_face:
        raise HTTPException(status_code=404, detail="Face not found")
    return db_face

@router.put("/{face_id}", response_model=schemas.face.FaceResponse)
def update_face(face_id: int, face: schemas.face.FaceUpdate, db: Session = Depends(get_db)):
    updated_face = services.face_service.update_face(db, face_id, face)
    if not updated_face:
        raise HTTPException(status_code=404, detail="Face not found")
    return updated_face

@router.delete("/{face_id}")
def delete_face(face_id: int, db: Session = Depends(get_db)):
    deleted_face = services.face_service.delete_face(db, face_id)
    if not deleted_face:
        raise HTTPException(status_code=404, detail="Face not found")
    return {"detail": "Face deleted successfully"}
