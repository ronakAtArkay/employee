from typing import List

from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session

from dependencies import get_db
from routers.admin.v1 import schemas
from routers.admin.v1.crud import employee

router = APIRouter()


@router.post("/department", tags=["department"])
def create_department(name: schemas.DepartmentBase, db: Session = Depends(get_db)):
    data = employee.create_department(name=name, db=db)
    return data


@router.post("/designation/{department_id}", tags=["designation"])
def create_designation(
    name: schemas.DesignationBase,
    department_id: str = Path(min_length=36, max_length=36),
    db: Session = Depends(get_db),
):
    data = employee.create_designation(department_id=department_id, name=name, db=db)
    return data


@router.post(
    "/create_employee/{designation_id}",
    response_model=schemas.ShowEmployeeBase,
    tags=["employee"],
)
def create_employee(
    detail: schemas.EmployeeBase,
    designation_id: str = Path(min_length=36, max_length=36),
    db: Session = Depends(get_db),
):
    data = employee.create_employee(designation_id=designation_id, detail=detail, db=db)
    return data


@router.get(
    "/get_employee/{id}", response_model=schemas.ShowEmployeeBase, tags=["employee"]
)
def get_employee(
    id: str = Path(min_length=36, max_length=36), db: Session = Depends(get_db)
):
    data = employee.get_employee_id(id=id, db=db)
    return data


@router.get(
    "/employees", response_model=List[schemas.ShowEmployeeBase], tags=["employee"]
)
def get_employee(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    data = employee.get_limited_employee(skip=skip, limit=limit, db=db)
    return data


@router.put(
    "/update_employee/{id}/{designation_id}", response_model=schemas.ShowEmployeeBase, tags=["employee"]
)
def update_employee(
    emp: schemas.EmployeeBase,
    designation_id: str = Path(min_length=36, max_length=36),
    id: str = Path(min_length=36, max_length=36),
    db: Session = Depends(get_db),
):
    data = employee.update_employee(
        emp=emp, designation_id=designation_id, id=id, db=db
    )
    return data


@router.delete("/delete_employee/{id}", tags=["employee"])
def delete_employee(
    id: str = Path(min_length=36, max_length=36), db: Session = Depends(get_db)
):
    data = employee.delete_employee(id=id, db=db)
    return data
