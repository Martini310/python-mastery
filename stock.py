import csv


class Stock:
    _types = (str, int, float)

    __slots__ = ('name', '_shares', '_price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, self._types[1]):
            raise TypeError(f"Expected {self._types[1].__name__}")
        if value < 0:
            raise ValueError("shares must be >= 0")
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, self._types[2]):
            raise TypeError(f"Expected {self._types[2].__name__}")
        if value < 0:
            raise ValueError("price must be >= 0")
        self._price = value

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares


def read_portfolio(filename, cls):
    output = []
    with open(filename) as f:
        file = csv.reader(f)
        headers = next(file)
        for row in file:
            output.append(cls.from_row(row))
    return output


def print_portfolio(portfolio):
    print('%10s %10s %10s' % ('name', 'shares', 'price'))
    print(('-'*10 + ' ')*3)

    for s in portfolio:
        print(f'{s.name:>10} {s.shares:>10} {s.price:>10}')


from decimal import Decimal


class DStock(Stock):
    types = (str, int, Decimal)


if __name__ == '__main__':
    portfolio = read_portfolio('Data/portfolio.csv', DStock)
    print_portfolio(portfolio)
    a = Stock('test', 22, 1.9)
    row = ['AA', '100', '32.20']
    s = DStock.from_row(row)
    print(s.name)
    print(s.shares)
    print(s.price)
    print(s.cost)

