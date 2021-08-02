import pets
class Ninja:
    # implement __init__(first_name, last_name, treats, pet_food, pet )
    def __init__(self, first_name, last_name, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food

    # implement the following methods:
    def get_pet(self, name, type, tricks):
        self.pet = pets.Pet(name, type, tricks)
        return self
    # walk() - walks the ninja's pet invoking the play method

    def walk(self):
        print('Walking pet....')
        pets.Pet.play(self.pet)
        return self
    # feed() - feeds the ninja's pet invoking the pet eat() method

    def feed(self):
        print(f'Feeding pet with {self.treats} and {self.pet_food}')
        pets.Pet.eat(self.pet)
        return self

    # bathe() - cleans the ninja's pet invoking the pet noise() method

    def bathe(self):
        print('Washing pet...')
        pets.Pet.noise(self.pet)
        return self

new_ninja = Ninja('Patrick', 'Dewey', 'weird treat', 'steak & lobster')
print(new_ninja)
new_ninja.get_pet('Fido', 'Dog', 'Rollover')
print(new_ninja.pet.health)
new_ninja.walk().feed().bathe()
print(new_ninja.pet.health)

new_dog = pets.Dog('Jerry', 'rollover')
print(new_dog.name)
