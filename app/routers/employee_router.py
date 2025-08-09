from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.schemas.employee import EmployeeResponse
from app.services.employee_service import (get_employee_by_uuid,
)

router = APIRouter(prefix="/employees", tags=["Employees"])

@router.get("/{emp_uuid}", response_model=EmployeeResponse)
def get_employee(emp_uuid: str, db: Session = Depends(get_db)):
    db_employee = get_employee_by_uuid(db, emp_uuid)
    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_employee