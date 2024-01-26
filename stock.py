from structure import Structure


class Stock(Structure):
    _fields = ('name', 'shares', 'price')

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares


Stock.create_init()

if __name__ == '__main__':

    s = Stock(name='GOOG', price=490.1, shares=50)
    print(s.name)
    print(s.shares)
    s = Stock('GOOG', 490.1, 50)
    print(s.name)
    print(s.shares)
    # s.share = 234

