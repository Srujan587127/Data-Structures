class Fruit:
    fruit_count = 0
    def __init__(self, color, taste, shape, preference):
        self.color = color
        self.shape = shape
        self.taste = taste 
        self.preference = preference

        Fruit.fruit_count += 1
        self.fruit_number = Fruit.fruit_count

    def get_shape(self):
        return self.shape
    
    def set_shape(self, new_shape):
        self.shape = new_shape

    def increase_preference(self):
        self.preference = self.preference + 1

    def showFruit(self):
        self.preference = self.preference + 1

    def showFruit(self):
        print(f"This is Fruit {self.fruit_number}")
        print(f"Color: {self.color}, Shape: {self.shape}, Taste: {self.taste}, Preferences: {self.preference}")
        print("-" * 40)

apple = Fruit("red", "sweet", "round", 1)
apple.showFruit()
apple.increase_preference()

print("shape of Fruit: ", apple.fruit_number, ":", apple.get_shape())
apple.set_shape("sphere")
apple.showFruit()

banana = Fruit("Yellow", "sweet", "cylinder", 2)
banana.showFruit()
banana.increase_preference()
banana.showFruit()
