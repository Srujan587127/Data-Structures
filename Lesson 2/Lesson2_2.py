# Multiple Inheritance - More than one parent class and one child class

#Prent class 1

class Salary:
    def __init__(self, salary):
        self.salary = salary

    def showSalary(self):
        print(f"Salary: {self.salary}")



#Parent class 2


class Benefits:
    def __init__(self, insurance):
        self.insurance= insurance 

    def showBenefits(self):
        print(f"Insurance Plans: {self.insurance}")


#Child Class


class Manager(Salary, Benefits):
    def __init__(self, name, salary, insurance):
        Salary.__init__(self, salary)
        Benefits.__init__(self, insurance)
        self.name = name 

    def displayDetails(self):
        print(f"Manager Name: {self.name}")
        self.showSalary()
        self.showBenefits()


man = Manager("Sarah Johnson", 10000, "Pemium Health Cover")
man.displayDetails()