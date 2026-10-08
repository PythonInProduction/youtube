class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShoppingCart:
    def __init__(self, items):
        self.items = items

    @property
    def total(self):
        return sum(item.price for item in self.items)
