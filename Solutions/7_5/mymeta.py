# mymeta.py

class mytype(type):
    @staticmethod
    def __new__(meta, name, bases, __dict__):
        print("Creating class :", name)
        print("Base classes   :", bases)
        print("Attributes     :", list(__dict__.keys()))
        return super().__new__(meta, name, bases, __dict__)

class myobject(metaclass=mytype):
    pass

class Stock(myobject):
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares*self.price
    def sell(self,nshares):
        self.shares -= nshares

class MyStock(Stock):
    pass
