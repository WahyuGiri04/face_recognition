from sqlalchemy.orm import Session
from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate, EmployeeUpdate

def create(db: Session, employee: EmployeeCreate):
    db_employee = Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Employee).filter(Employee.is_deleted == False).offset(skip).limit(limit).all()

def get_by_id(db: Session, emp_id: int):
    return db.query(Employee).filter(Employee.id == emp_id, Employee.is_deleted == False).first()

def get_by_email(db: Session, email: str):
    return db.query(Employee).filter(Employee.email == email, Employee.is_deleted == False).first()

def update(db: Session, db_employee: Employee, employee_data: EmployeeUpdate):
    update_data = employee_data.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_employee, key, value)
    db.commit()
    db.refresh(db_employee)
    return db_employee

def delete(db: Session, db_employee: Employee):
    db_employee.is_deleted = True
    db.commit()
    db.refresh(db_employee)
    return db_employee