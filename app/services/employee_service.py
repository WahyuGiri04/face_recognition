from sqlalchemy.orm import Session
from app.repositories.employee_repository import create, get_all, get_by_id, update, delete
from app.schemas.employee import EmployeeCreate, EmployeeUpdate

def create_employee(db: Session, employee: EmployeeCreate):
    return create(db, employee)

def get_all_employees(db: Session, skip: int = 0, limit: int = 100):
    return get_all(db, skip, limit)

def get_employee_by_id(db: Session, emp_id: int):
    return get_by_id(db, emp_id)

def update_employee(db: Session, emp_id: int, employee: EmployeeUpdate):
    db_employee = get_by_id(db, emp_id)
    if not db_employee:
        return None
    return update(db, db_employee, employee)

def delete_employee(db: Session, emp_id: int):
    db_employee = get_by_id(db, emp_id)
    if not db_employee:
        return None
    return delete(db, db_employee)