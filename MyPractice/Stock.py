import csv

class Stock:

    

    def __init__(self,name,stock,price):
        
        self.stock=stock
        self.price=price
        self.name=name
    
        

    def get_total_cost(self):

        
        return self.stock * self.price
    

stock_1=Stock("IBM",23,234)

print(stock_1.get_total_cost())

