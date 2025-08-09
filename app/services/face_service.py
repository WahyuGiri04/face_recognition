from sqlalchemy.orm import Session
from app.repositories.face_repository import create, get_all, get_by_id, update, delete
from app.schemas.face import FaceCreate, FaceUpdate

def create_face(db: Session, face: FaceCreate):
    return create(db, face)

def get_all_faces(db: Session, skip: int = 0, limit: int = 100):
    return get_all(db, skip, limit)

def get_face_by_id(db: Session, face_id: int):
    return get_by_id(db, face_id)

def update_face(db: Session, face_id: int, face: FaceUpdate):
    db_face = get_by_id(db, face_id)
    if not db_face:
        return None
    return update(db, db_face, face)

def delete_face(db: Session, face_id: int):
    db_face = get_by_id(db, face_id)
    if not db_face:
        return None
    return delete(db, db_face)