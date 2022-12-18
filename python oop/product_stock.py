

class ProductStock:

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def name(self):
        return self.product.name

    def unit_price(self):
        return self.product.price

    def cost(self):
        return self.unit_price() * self.quantity

    def __repr__(self):
        return f"{self.product} QUANTITY: {self.quantity}"
