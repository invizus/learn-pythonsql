#!/usr/bin/env python3

class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department
    def info(self):
        return f"{self.name} {self.department}"

Messi = Employee(department="manager", name="Messi")
#Messi = Employee("Messi", "manager")
print(Messi.info())
