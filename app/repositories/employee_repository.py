from sqlalchemy.orm import Session
from app import models, schemas

def create(db: Session, employee: schemas.employee.EmployeeCreate):
    new_employee = models.employee.Employee(**employee.dict())
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.employee.Employee).offset(skip).limit(limit).all()

def get_by_id(db: Session, emp_id: int):
    return db.query(models.employee.Employee).filter(models.employee.Employee.id == emp_id).first()

def update(db: Session, db_employee, employee_data: schemas.employee.EmployeeUpdate):
    for key, value in employee_data.dict(exclude_unset=True).items():
        setattr(db_employee, key, value)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def delete(db: Session, db_employee):
    db.delete(db_employee)
    db.commit()
    return db_employee
