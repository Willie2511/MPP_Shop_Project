
class Product:

    def __init__(self, name, price=0):
        self.name = name
        self.price = price

    def __repr__(self):
        return f'NAME: {self.name} PRICE: {self.price}'
