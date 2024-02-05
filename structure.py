from validate import Validator, validated


def validate_attributes(cls):
    """
    Class decorator that scans a class definition for Validators
    and builds a _fields variable that captures their definition order.
    """
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)

        # Apply validated decorator to any callable with annotations
        elif callable(val) and val.__annotations__:
            setattr(cls, name, validated(val))

    # Collect all of the field names
    cls._fields = [val.name for val in validators]

    # Collect type conversions. The lambda x:x is an identity
    # function that's used in case no expected_type is found.
    cls._types = tuple([getattr(v, 'expected_type', lambda x: x)
                        for v in validators])

    # Create the __init__ method
    if cls._fields:
        cls.create_init()

    return cls


class Structure:
    _fields = ()
    _types = ()

    def __setattr__(self, name, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError(f'No attribute {name}')

    def __repr__(self):
        return f"{type(self).__name__}{tuple(getattr(self, name) for name in self._fields)}"

    @classmethod
    def from_row(cls, row):
        rowdata = [func(val) for func, val in zip(cls._types, row)]
        return cls(*rowdata)

    @classmethod
    def create_init(cls):
        """
        Create an __init__ method from _fields
        """
        argstr = ', '.join(cls._fields)
        code = f'def __init__(self, {argstr}):\n'
        for field in cls._fields:
            code += f'    self.{field} = {field}\n'
        locs = {}
        exec(code, locs)
        cls.__init__ = locs['__init__']

    @classmethod
    def __init_subclass__(cls):
        # Apply the validated decorator to subclasses
        validate_attributes(cls)


def typed_structure(clsname, **validators):
    cls = type(clsname, (Structure,), validators)
    return cls


if __name__ == '__main__':
    from validate import String, PositiveInteger, PositiveFloat
    Stock = typed_structure('Stock', name=String(), shares=PositiveInteger(), price=PositiveFloat())
    s = Stock('GOOG', 100, 490.1)
    print(s.name)
    print(s)
    Stock('GOOG', 100, 490.1)
