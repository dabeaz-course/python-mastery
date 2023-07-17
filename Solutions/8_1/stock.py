# stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    name = String('name')
    shares = PositiveInteger('shares')
    price = PositiveFloat('price')

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

if __name__ == '__main__':
    from reader import read_csv_as_instances
    from tableformat import create_formatter, print_table
    
    portfolio = read_csv_as_instances('../../Data/portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name','shares','price'], formatter)
