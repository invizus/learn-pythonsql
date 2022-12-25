#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Employee(Base):
    __tablename__ = "employee"

    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    department = Column(String(20))

    def __init__(self, name, department):
        self.name = name
        self.department = department
    def info(self):
        return f"{self.name} {self.department}"

#Messi = Employee(department="manager", name="Messi")
##Messi = Employee("Messi", "manager")
#print(Messi.info())

engine = create_engine("mysql+mysqlconnector://roman:passw0rd@localhost/clockin")
Base.metadata.create_all(engine)

u1 = Employee(name="Roman", department="IT")
#print(u1(info))
Session = sessionmaker(bind=engine)
session = Session()
session.add(u1)
session.commit()
