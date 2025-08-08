from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from services.employee_service import EmployeeService
from repositories.employee_repository import EmployeeRepository
from schemas.base_response import BaseResponse
from schemas.employee_schema import EmployeeResponse

router = APIRouter(prefix="/employees", tags=["Employee"])

@router.get("/", response_model=BaseResponse[list[EmployeeResponse]])
def list_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    repo = EmployeeRepository(db)
    service = EmployeeService(repo)
    data = service.get_all_employees(skip, limit)
    return BaseResponse(status_code=200, message="Success", data=data)

@router.get("/{emp_id}", response_model=BaseResponse[EmployeeResponse])
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    repo = EmployeeRepository(db)
    service = EmployeeService(repo)
    emp = service.get_employee_by_id(emp_id)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return BaseResponse(status_code=200, message="Success", data=emp)