class Store:
    def __init__(self, name):
        self.name = name
        self.list_of_products = []

    def add_product(self, new_product):
        self.list_of_products.append(new_product)
        return self

    def sell_product(self, id):
        self.list_of_products.pop(list_of_products[id])
        return self

    def inflation(self, percent_increase):
        Products.update_price(percent_change, True)
        return self

    def set_clearance(self, category, percent_discount):
        for i in self.list_of_products:
            if i['product_category'] == category:
                i['product_price'] *= percent_discount
        return self


class Products:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def add_product(self, new_product, store):
        new_product = {
            "product_name": self.name,
            "product_price": self.price,
            "product_category": self.category
        }
        store.list_of_products.append(new_product)
        return self
    def update_price(self, percent_change, is_increased):
        if(is_increased):
            self.price = self.price * (1 + percent_change)
        else:
            self.price = self.price * (1 - percent_change)
        return self
    def print_info(self):
        print(
            f"The name of the product is {self.name}.\nThe category is {self.category}. \nThe price is {self.price}")
        return self

cupcake_store = Store("NYCcupcake")
cupcake = Products('cupcake', 80, 'baking')
cheesecake = Products('cheesecake', 70, 'dessert'  )
print(cupcake_store)
print(Products)
cupcake.add_product(cupcake, cupcake_store)
cheesecake.add_product(cheesecake, cupcake_store)
for i in cupcake_store.list_of_products:
    print(i['product_name'], i['product_price'], i['product_category'])

cupcake_store.set_clearance("dessert", 0.8)
for i in cupcake_store.list_of_products:
    print(i['product_name'], i['product_price'], i['product_category'])
