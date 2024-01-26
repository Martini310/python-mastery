import sys
import inspect


class Structure:
    _fields = ()

    def __repr__(self):
        return f"{type(self).__name__}{tuple(getattr(self, name) for name in self._fields)}"

    def __setattr__(self, name, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError(f'No attribute {name}')

    @classmethod
    def create_init(cls):
        argstr = ', '.join(cls._fields)
        code = f'def __init__(self, {argstr}):\n'
        for field in cls._fields:
            code += f'    self.{field} = {field}\n'
        locs = {}
        exec(code, locs)
        cls.__init__ = locs['__init__']


if __name__ == '__main__':

    def add(x, y):
        """Adds two things"""
        return x + y


    from collections import namedtuple
    Stock = namedtuple('Stock', ['name', 'shares', 'price'])
    s = Stock('GOOG', 100, 490.1)
    print(s.name)

    print(s.shares)

    print(s[1])
    import inspect
    print(inspect.getsource(namedtuple))
