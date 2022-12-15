import datetime
from enum import Enum

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship

from database import Base
from libs.utils import date

# class emp_department:
#     marketing = "marketing"
#     production = "production"
#     accounting = "accounting"
#     bus_analyst = "bus_analyst"
#     testing = "testing"

# class marketing:
#     chif_marketing_officer = "chif_marketing_officer"
#     marketing_manager = "marketing_manager"
#     sales_representative = "sales_representative"
#     sales_man = "sales_man"

# class production:
#     ch


class DepartmentModel(Base):
    __tablename__ = "department"

    id = Column(String(36), primary_key=True)
    name = Column(String(200), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now)
    is_deleted = Column(Boolean, default=False)


class DesignationModel(Base):
    __tablename__ = "designation"

    id = Column(String(36), primary_key=True)
    department_id = Column(String(200), ForeignKey("department.id"))
    name = Column(String(200))
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now)
    is_deleted = Column(Boolean, default=False)

    department = relationship("DepartmentModel", backref="designation")


class EmployeeModel(Base):
    __tablename__ = "employee"

    id = Column(String(36), primary_key=True)
    designation_id = Column(String(200), ForeignKey("designation.id"))
    name = Column(String(200), nullable=True)
    city = Column(String(200), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now)
    is_deleted = Column(Boolean, default=False)

    designation = relationship("DesignationModel", backref="employee")
