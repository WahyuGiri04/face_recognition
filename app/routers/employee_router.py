from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.schemas.employee import EmployeeCreate, EmployeeUpdate, EmployeeResponse
from app.services.employee_service import (
    create_employee, get_all_employees, get_employee_by_id, 
    update_employee, delete_employee
)

router = APIRouter(prefix="/employees", tags=["Employees"])

@router.post("/", response_model=EmployeeResponse)
def create_employee_endpoint(employee: EmployeeCreate, db: Session = Depends(get_db)):
    return create_employee(db, employee)

@router.get("/", response_model=List[EmployeeResponse])
def get_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_all_employees(db, skip, limit)

@router.get("/{emp_id}", response_model=EmployeeResponse)
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    db_employee = get_employee_by_id(db, emp_id)
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee

@router.put("/{emp_id}", response_model=EmployeeResponse)
def update_employee_endpoint(emp_id: int, employee: EmployeeUpdate, db: Session = Depends(get_db)):
    updated_employee = update_employee(db, emp_id, employee)
    if not updated_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated_employee

@router.delete("/{emp_id}")
def delete_employee_endpoint(emp_id: int, db: Session = Depends(get_db)):
    deleted_employee = delete_employee(db, emp_id)
    if not deleted_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"detail": "Employee deleted successfully"}