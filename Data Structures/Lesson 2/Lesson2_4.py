# Hierarchial One parent class and multiple child classes

#Parent Class

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
    
    def show_brand(self):
        print(f"Brand: {self.brand}")



#Child Class 1

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display_car(self):
        self.show_brand()
        print(f"Car Model : {self.model}")



#Child class 2
class Bike(Vehicle):
    def __init__(self, brand, engine_cc):
        super().__init__(brand)
        self.engine_cc = engine_cc

    def display_bike(self):
        self.show_brand()
        print(f"Engine Capacity: {self.engine_cc}")


car = Car("Mercedes", "G-Class")
bike = Bike("BMW", "400cc")

car.display_car()
print()
bike.display_bike()
