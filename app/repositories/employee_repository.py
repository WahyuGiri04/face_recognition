from sqlalchemy.orm import Session
from app.models.employee import Employee

def get_by_uuid(db: Session, emp_uuid: str):
    return db.query(Employee).filter(Employee.uuid == emp_uuid, Employee.is_deleted == False).first()
