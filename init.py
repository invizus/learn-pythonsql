#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

print("This script will init database\n")

engine = create_engine("mysql+mysqlconnector://roman:passw0rd@localhost/clockin")
print(database_exists(engine.url))
#create_database(engine.url)
