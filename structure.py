import sys
import inspect


class Structure:
    _fields = ()

    @staticmethod
    def _init():
        locs = sys._getframe(1).f_locals
        self = locs.pop('self')
        print(locs)
        for name, val in locs.items():
            setattr(self, name, val)

    def __repr__(self):
        return f"{type(self).__name__}{tuple(getattr(self, name) for name in self._fields)}"

    def __setattr__(self, name, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError(f'No attribute {name}')

    @classmethod
    def set_fields(cls):
        sig = inspect.signature(cls)
        cls._fields = tuple(sig.parameters)



if __name__ == '__main__':

    def add(x, y):
        """Adds two things"""
        return x + y
