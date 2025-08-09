from sqlalchemy.orm import Session
from app.repositories import employee_repository
from app import schemas

def create_employee(db: Session, employee: schemas.employee.EmployeeCreate):
    return employee_repository.create(db, employee)

def get_all_employees(db: Session, skip: int = 0, limit: int = 100):
    return employee_repository.get_all(db, skip, limit)

def get_employee_by_id(db: Session, emp_id: int):
    return employee_repository.get_by_id(db, emp_id)

def update_employee(db: Session, emp_id: int, employee: schemas.employee.EmployeeUpdate):
    db_employee = employee_repository.get_by_id(db, emp_id)
    if not db_employee:
        return None
    return employee_repository.update(db, db_employee, employee)

def delete_employee(db: Session, emp_id: int):
    db_employee = employee_repository.get_by_id(db, emp_id)
    if not db_employee:
        return None
    return employee_repository.delete(db, db_employee)
