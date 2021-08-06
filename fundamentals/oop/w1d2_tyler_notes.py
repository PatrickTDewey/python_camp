class User:
    pass

class Car():
    def __init__(self):
        self.model = "Tesla"
        self.color = "Hot Pink"
        self.flames = "Gold"

patricks_car = Car()
vincent_car = Car()

print(patricks_car.color)
print(vincent_car.color)
patricks_car.color = "Black"
print(patricks_car.color)
