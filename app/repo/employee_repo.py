from sqlalchemy.orm import Session
from models.employee import Employee

class EmployeeRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, skip: int = 0, limit: int = 100):
        return self.db.query(Employee).filter(Employee.is_deleted == False).offset(skip).limit(limit).all()

    def get_by_id(self, emp_id: int):
        return self.db.query(Employee).filter(
            Employee.id == emp_id,
            Employee.is_deleted == False
        ).first()