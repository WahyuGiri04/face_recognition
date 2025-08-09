from sqlalchemy.orm import Session
from app.repositories.employee_repository import get_by_uuid


def get_employee_by_uuid(db: Session, emp_uuid: str):
    return get_by_uuid(db, emp_uuid)
