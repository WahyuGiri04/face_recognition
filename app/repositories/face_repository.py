from sqlalchemy.orm import Session
from app.models.face import Face
from app.schemas.face import FaceCreate, FaceUpdate

def create(db: Session, face: FaceCreate):
    db_face = Face(**face.dict())
    db.add(db_face)
    db.commit()
    db.refresh(db_face)
    return db_face

def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Face).filter(Face.is_deleted == False).offset(skip).limit(limit).all()

def get_by_id(db: Session, face_id: int):
    return db.query(Face).filter(Face.id == face_id, Face.is_deleted == False).first()

def get_by_employee_id(db: Session, employee_id: int):
    return db.query(Face).filter(Face.employee_id == employee_id, Face.is_deleted == False).all()

def update(db: Session, db_face: Face, face_data: FaceUpdate):
    update_data = face_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_face, key, value)
    db.commit()
    db.refresh(db_face)
    return db_face

def delete(db: Session, db_face: Face):
    db_face.is_deleted = True
    db.commit()
    db.refresh(db_face)
    return db_face