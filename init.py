#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String

print("This script will init database\n")

engine = create_engine("mysql+mysqlconnector://roman:passw0rd@localhost/clockin")
print(database_exists(engine.url))
#create_database(engine.url)

metadata_obj = MetaData()

employees = Table(
    "employees",
    metadata_obj,
    Column("employee_id", Integer, primary_key=True),
    Column("employee_name", String(60), nullable=False),
    Column("department", String(20)),
)

employees.create(engine)
