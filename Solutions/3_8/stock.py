# stock.py

class Stock:
    __slots__ = ('name','_shares','_price')
    _types = (str, int, float)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        # Note: The !r format code produces the repr() string
        return f'{type(self).__name__}({self.name!r}, {self.shares!r}, {self.price!r})'

    def __eq__(self, other):
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) ==
                (other.name, other.shares, other.price))

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)

    @property
    def shares(self):
        return self._shares
    @shares.setter
    def shares(self, value):
        if not isinstance(value, self._types[1]):
            raise TypeError(f'Expected {self._types[1].__name__}')
        if value < 0:
            raise ValueError('shares must be >= 0')
        self._shares = value

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        if not isinstance(value, self._types[2]):
            raise TypeError(f'Expected {self._types[2].__name__}')
        if value < 0:
            raise ValueError('price must be >= 0')
        self._price = value

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

# Sample
if __name__ == '__main__':
    import tableformat
    import reader
    from tableformat import (
        print_table,
        create_formatter,
        TextTableFormatter,
        ColumnFormatMixin,
        UpperHeadersMixin
        )

    portfolio = reader.read_csv_as_instances('../../Data/portfolio.csv', Stock)

    class PortfolioFormatter(ColumnFormatMixin, TextTableFormatter):
        formats = ['%s','%d','%0.2f']

    formatter = PortfolioFormatter()
    print_table(portfolio,['name','shares','price'], formatter)

    class PortfolioFormatter(UpperHeadersMixin, TextTableFormatter):
        pass

    formatter = PortfolioFormatter()
    print_table(portfolio, ['name','shares','price'], formatter)

    # Factory function version
    formatter = create_formatter('text', column_formats=['%s','%d','%0.2f'])
    print_table(portfolio, ['name','shares','price'], formatter)

    formatter = create_formatter('text', upper_headers=True)
    print_table(portfolio, ['name','shares','price'], formatter)
