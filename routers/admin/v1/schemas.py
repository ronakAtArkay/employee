from datetime import datetime

from pydantic import BaseModel


class DepartmentBase(BaseModel):
    name: str


class Department(BaseModel):
    # id : str
    name: str

    class Config:
        orm_mode = True


class DesignationBase(BaseModel):
    name: str


class Designation(BaseModel):
    # id : str
    # department_id : str
    name: str
    department: Department

    class Config:
        orm_mode = True


class EmployeeBase(BaseModel):
    name: str
    city: str


class UpdateEmpBase(BaseModel):
    designation_id: str
    name: str
    city: str


class ShowEmployeeBase(BaseModel):
    id: str
    # designation_id: str
    name: str
    city: str
    designation: Designation
    created_at: datetime
    updated_at: datetime
    is_deleted: bool

    class Config:
        orm_mode = True
