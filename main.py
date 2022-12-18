#!/usr/bin/python3

class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department
    def info(self):
        return f"{self.name} {self.department}"

#Smita = Employee(department="manager", name="Smita")
Smita = Employee("smita", "manager")
print(Smita.info())
