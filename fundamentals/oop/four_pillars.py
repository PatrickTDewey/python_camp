class CoffeeM:
    def __init__(self, name):
        self.name = name
        self.water_temp = 200

    def brew_now(self, beans):
        print(f'Using {beans}!')
        print('brew now brown cow..')
        return self

    def clean(self):
        print('Cleaning!')
        return self


class CappuccinoM(CoffeeM):
    def __init__(self, name):
        super().__init__(name)
        self.milk = "whole"

    def make_cappuccino(self, beans):
        super().brew_now(beans)
        print("Frothy!!!")

    def clean(self):
        print("Cleaning the froth, but not really, I'm just a print statement")


the_first_coffee = CoffeeM('Coffe 1')
new_coffee = CappuccinoM('cino_1')


class Barista:
    def __init__(self, name):
        self.name = name
        self.cafe = CoffeeM("Cafe")

    def make_coffee(self, beans):
        self.cafe.brew_now(beans)


new_barista = Barista('Jared')
print(the_first_coffee)
print(new_coffee)

new_coffee.clean()

new_coffee.make_cappuccino('black')
new_barista.make_coffee('black')