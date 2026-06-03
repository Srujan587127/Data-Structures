class Car:
    def __init__(self, color, brand, model):
        self.color = color
        self.brand = brand
        self.model = model

    def Start(self):
        print("Car has started. ")

    def Stop(self):
        print("Car has stopped. ")

    def display_details(self):
        print("Car Details: ")
        print("Brand: ", self.brand)
        print("Model: ", self.model)
        print("Color: ", self.color)

mycar = Car("Black", "Toyota", "SUV")
mycar.display_details()
mycar.Start()
mycar.Stop()