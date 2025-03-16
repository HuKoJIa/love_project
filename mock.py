from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column


class Base(DeclarativeBase):
    pass 

class Company(Base):
    __tablename__ = "company"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    employees: Mapped[list["Employee"]] = relationship("Employee", back_populates="company")


class Employee(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    company_id: Mapped[int] = mapped_column(ForeignKey("company.id", nullable=False))
    company: Mapped[Company] = relationship("Company", back_populates="employees")

"""
    CREATE TABLE Company
    (
        id int GENERATED ALWAYS AS INDENTITY PRIMARY KEY,
        name VARCHAR(256) NOT NULL,
    )

    CREATE TABLE employee
    (
        id int GENERATED ALWAYS AS INDENTITY PRIMARY KEY,
        name VARCHAR(256) NOT NULL,
        company_id int,
        FOREIGN KEY (company_id) REFERENCES company(id)
    )
"""