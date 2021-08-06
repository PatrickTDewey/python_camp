class Store:
    def __init__(self, name):
        self.products = []
        self.name = name
    def add_product(self, new_product):
        self.products.append(new_product)
        return self

    def sell_product(self, id):
        print(f'Selling Product: {self.products[id].name} for price: {self.products[id].price}')
        self.products.pop(id)
        return self
    
    def inflation(self, percent_increase):
        for i in self.products:


class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased:
            self.price += (self.price * percent_change)
        else:
            self.price -= (self.price * percent_change)
        return self
    def print_info(self):
        print('Name: %s Category: %s Price: %d' %(self.name, self.category, self.price))
        return self

garden_hoe = Product('Garden Hoe', 89, 'Gardening')
garden_hoe.print_info()

walmart = Store('Walmart')
print(walmart.name)
print(walmart.products)
walmart.add_product(garden_hoe)
for i in walmart.products:
    print(i.name)
walmart.sell_product(0)
print(walmart.products)