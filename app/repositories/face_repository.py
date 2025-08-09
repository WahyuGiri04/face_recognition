from sqlalchemy.orm import Session
from app import models, schemas

def create(db: Session, face: schemas.face.FaceCreate):
    new_face = models.face.Face(**face.dict())
    db.add(new_face)
    db.commit()
    db.refresh(new_face)
    return new_face

def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.face.Face).offset(skip).limit(limit).all()

def get_by_id(db: Session, face_id: int):
    return db.query(models.face.Face).filter(models.face.Face.id == face_id).first()

def update(db: Session, db_face, face_data: schemas.face.FaceUpdate):
    for key, value in face_data.dict(exclude_unset=True).items():
        setattr(db_face, key, value)
    db.commit()
    db.refresh(db_face)
    return db_face

def delete(db: Session, db_face):
    db.delete(db_face)
    db.commit()
    return db_face
