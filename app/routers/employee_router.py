from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.schemas.employee import EmployeeResponse
from app.schemas.base_response import BaseResponse
from app.services.employee_service import get_employee_by_uuid
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter(prefix="/employees", tags=["Employees"])

@router.get("/{emp_uuid}", response_model=BaseResponse[EmployeeResponse])
def get_employee(emp_uuid: str, db: Session = Depends(get_db)):
    try:
        # Validate UUID format
        if not emp_uuid or len(emp_uuid.strip()) == 0:
            return BaseResponse.bad_request("Employee UUID is required")
        
        db_employee = get_employee_by_uuid(db, emp_uuid)
        
        if not db_employee:
            logger.info(f"Employee with UUID {emp_uuid} not found")
            return BaseResponse.not_found(f"Employee with UUID {emp_uuid} not found")
        
        logger.info(f"Employee {emp_uuid} retrieved successfully")
        return BaseResponse.success(
            data=db_employee,
            message="Employee retrieved successfully"
        )
        
    except ValueError as ve:
        logger.error(f"ValueError in get_employee: {str(ve)}")
        return BaseResponse.bad_request(f"Invalid UUID format: {str(ve)}")
    
    except Exception as e:
        logger.error(f"Internal server error in get_employee: {str(e)}")
        return BaseResponse.error("An unexpected error occurred while retrieving employee data")