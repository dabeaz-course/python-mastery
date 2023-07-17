# stock.py

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares


def read_portfolio(filename):
    '''
    Read a CSV file of stock data into a list of Stocks
    '''
    import csv
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = Stock(row[0], int(row[1]), float(row[2]))
            portfolio.append(record)
    return portfolio

if __name__ == '__main__':
    import tableformat
    portfolio = read_portfolio('../../Data/portfolio.csv')
    tableformat.print_table(portfolio, ['name','shares','price'])
