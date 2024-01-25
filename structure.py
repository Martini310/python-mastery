class Structure:
    _fields = ()

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, arg in zip(self._fields, args):
            setattr(self, name, arg)

    def __repr__(self):
        return f"{type(self).__name__}{tuple(getattr(self, name) for name in self._fields)}"

    def __setattr__(self, name, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError(f'No attribute {name}')


class Stock(Structure):
    _fields = ('name','shares','price')


class Date(Structure):
    _fields = ('year', 'month', 'day')


if __name__ == '__main__':
    s = Stock('GOOG', 100, 490.1)
    print(s.name)
    print(s.shares)
    print(s.price)
    # s = Stock('AA',50)
    print(repr(s))
    s.shares = 50
    s.share = 50
    s._shares = 100
