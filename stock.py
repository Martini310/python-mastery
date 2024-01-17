

class Stock:
    _types = (str, int, float)

    __slots__ = ('name', '_shares', '_price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        # Note: The !r format code produces the repr() string
        return f"{type(self).__name__}({self.name!r}, {self.shares!r}, {self.price!r})"

    def __eq__(self, other):
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) ==
                                             (other.name, other.shares, other.price))

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


class DStock(Stock):
    from decimal import Decimal
    types = (str, int, Decimal)


if __name__ == '__main__':
    import reader
    from tableformat import create_formatter, print_table

    portfolio = reader.read_csv_as_instances('../../Data/portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name', 'shares', 'price'], formatter)
