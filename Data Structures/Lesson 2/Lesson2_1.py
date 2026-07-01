# Single Inheritance

# Parent Class

class Employee:
    def __init__(self, empid, name):
        self.empid = empid
        self.name = name

    def displayEmployee(self):
        print(f"Employee ID: {self.empid}")
        print(f"Employee Name: {self.name}")



# Child Class


class Developer(Employee):
    def __init__(self, empid, name, progLang):
        super().__init__(empid, name)
        self.progLang = progLang

    def displayDeveloper(self):
        self.displayEmployee()
        print(f"Programming Language: {self.progLang}")



# Always create object of child class

dev = Developer("E101", "John Smith", "Python")
dev.displayDeveloper()
    