from fastapi import HTTPException, status
from sqlalchemy.orm import Session

import models
from libs.utils import date, generate_id
from routers.admin.v1 import schemas


def create_department(name: schemas.DepartmentBase, db: Session):
    db_department = models.DepartmentModel(id=generate_id(), name=name.name)
    db.add(db_department)
    db.commit()
    db.refresh(db_department)
    return db_department


def create_designation(department_id: str, name: schemas.DesignationBase, db: Session):
    db_designation = models.DesignationModel(
        id=generate_id(), department_id=department_id, name=name.name
    )
    db.add(db_designation)
    db.commit()
    db.refresh(db_designation)
    return db_designation


def create_employee(designation_id: str, detail: schemas.EmployeeBase, db: Session):
    db_employee = models.EmployeeModel(
        id=generate_id(),
        designation_id=designation_id,
        name=detail.name,
        city=detail.city,
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def get_Detail(db: Session, id: str):
    db_detail = (
        db.query(models.EmployeeModel)
        .filter(models.EmployeeModel.id == id, models.EmployeeModel.is_deleted == False)
        .first()
    )
    return db_detail


def get_employee_id(db: Session, id: str):
    db_detail = get_Detail(db=db, id=id)
    if db_detail is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found"
        )
    db_emp = (
        db.query(models.EmployeeModel)
        .join(models.DesignationModel, models.DepartmentModel)
        .filter(models.DesignationModel.id == models.EmployeeModel.designation_id)
        .first()
    )
    return db_emp


def get_limited_employee(db: Session, skip: int, limit: int):
    db_employee = (
        db.query(models.EmployeeModel)
        .filter(models.EmployeeModel.is_deleted == False)
        .offset(skip)
        .limit(limit)
        .all()
    )
    return db_employee


def update_employee(
    db: Session, id: str, designation_id: str, emp: schemas.EmployeeBase
):
    db_employee = get_Detail(id=id, db=db)
    if db_employee is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="employee not found"
        )
    db_employee.designation_id = designation_id
    db_employee.name = emp.name
    db_employee.city = emp.city
    db_employee.updated_at = date()
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee


def delete_employee(db: Session, id: str):
    db_employee = get_Detail(id=id, db=db)
    if db_employee is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Employee not found"
        )
    db_employee.is_deleted = True
    db_employee.updated_at = date()
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return f"{db_employee.name} employee is successfully deleted."
