import pets
class Ninja:
    # implement __init__(first_name, last_name, treats, pet_food, pet )
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    # walk() - walks the ninja's pet invoking the play method

    def walk(self):
        print('Walking pet....')
        self.pet.play()
        return self
    # feed() - feeds the ninja's pet invoking the pet eat() method

    def feed(self):
        print(f'Feeding pet with {self.treats} and {self.pet_food}')
        self.pet.eat()
        return self

    # bathe() - cleans the ninja's pet invoking the pet noise() method

    def bathe(self):
        print('Washing pet...')
        self.pet.noise()
        return self

fido = pets.Dog('Fido', 'rollover')
new_ninja = Ninja('Patrick', 'Dewey', 'weird treat', 'steak & lobster', fido)
print(new_ninja.pet.health)

new_ninja.walk()

print(new_ninja.pet.health)

# new_dog = pets.Dog('Jerry', 'rollover')
# print(new_dog.name)
