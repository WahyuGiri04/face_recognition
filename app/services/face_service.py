from sqlalchemy.orm import Session
from app.repositories import face_repository
from app import schemas

def create_face(db: Session, face: schemas.face.FaceCreate):
    return face_repository.create(db, face)

def get_all_faces(db: Session, skip: int = 0, limit: int = 100):
    return face_repository.get_all(db, skip, limit)

def get_face_by_id(db: Session, face_id: int):
    return face_repository.get_by_id(db, face_id)

def update_face(db: Session, face_id: int, face: schemas.face.FaceUpdate):
    db_face = face_repository.get_by_id(db, face_id)
    if not db_face:
        return None
    return face_repository.update(db, db_face, face)

def delete_face(db: Session, face_id: int):
    db_face = face_repository.get_by_id(db, face_id)
    if not db_face:
        return None
    return face_repository.delete(db, db_face)
