def typedproperty(name, expected_type):
    private_name = '_' + name

    @property
    def value(self):
        return getattr(self, private_name)

    @value.setter
    def value(self, val):
        if not isinstance(val, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, private_name, val)

    @property
    def __set_name__(self, cls, name):
        self.name = name

    return value


String = lambda name: typedproperty(name, str)
Integer = lambda name: typedproperty(name, int)
Float = lambda name: typedproperty(name, float)

if __name__ == '__main__':
    class Stock:
        name = String('name')
        shares = Integer('shares')
        price = Float('price')

        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price

    a = Stock('12', 12, 12.0)
    print(a)