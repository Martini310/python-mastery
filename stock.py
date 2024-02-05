from structure import Structure


class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares


# Stock.create_init()

if __name__ == '__main__':
    s = Stock.from_row(['GOOG', '100', '490.1'])
    print(s)
    import reader
    port = reader.read_csv_as_instances('Data/portfolio.csv', Stock)

