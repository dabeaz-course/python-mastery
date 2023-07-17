# stock.py

from structure import Structure

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

Stock.create_init()

