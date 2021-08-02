class Pet:
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 90
        self.energy = 0

    def sleep(self):
        if self.energy + 25 <= 100:
            self.energy += 25
        else:
            self.energy = 100
        return self

    def eat(self):
        if self.health + 10 <= 100:
            self.health += 10
        else:
            self.health = 100
        if self.energy + 5 <= 100:
            self.energy += 5
        else:
            self.energy = 100
        return self

    def play(self):
        if self.health + 5 <= 100:
            self.health += 5
        else:
            self.health = 100
        return self
    def noise(self):
        print('roof')

class Dog(Pet):
    def __init__(self, name, tricks, type='Dog'):
        super().__init__(name, type, tricks)
        
if __name__ == "__main__":
    print("the file is being executed directly")
else:
    print("The file is being executed because it is imported by another file. The file is called: ", __name__)
