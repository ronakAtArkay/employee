from datetime import datetime

from pydantic import BaseModel


class DepartmentBase(BaseModel):
    name: str


class DesignationBase(BaseModel):
    name: str


class EmployeeBase(BaseModel):
    name: str
    city: str


class ShowEmployeeBase(BaseModel):
    id: str
    designation_id: str
    name: str
    city: str
    created_at: datetime
    updated_at: datetime
    is_deleted: datetime

    class Config:
        orm_mode = True
