import csv
from product import *
from product_stock import *
from customer import *


class Shop:

    def __init__(self, path):
        self.stock = []
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            first_row = next(csv_reader)
            self.cash = float(first_row[0])
            for row in csv_reader:
                p = Product(row[0], float(row[1]))
                ps = ProductStock(p, float(row[2]))
                self.stock.append(ps)

    def __repr__(self):
        str = ""
        str += f'Shop has {self.cash} in cash\n'
        for item in self.stock:
            str += f"{item}\n"
        return str


s = Shop("../stock.csv")
# print(s)

c = Customer("../customer.csv")
c.calculate_costs(s.stock)
print(c)
