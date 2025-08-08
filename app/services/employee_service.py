from app.repo.employee_repo import EmployeeRepository

class EmployeeService:
    def __init__(self, repo: EmployeeRepository):
        self.repo = repo

    def get_all_employees(self, skip: int, limit: int):
        return self.repo.get_all(skip, limit)

    def get_employee_by_id(self, emp_id: int):
        return self.repo.get_by_id(emp_id)