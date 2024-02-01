from functools import wraps


def logformat(message):
    def logged(func):
        print('Adding logging to', func.__name__)

        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Calling', func.__name__)
            print(message.format(func=func))
            return func(*args, **kwargs)
        return wrapper
    return logged


if __name__ == '__main__':
    from validate import Integer, validated
    from inspect import signature


    @validated
    def add(x: Integer, y: Integer) -> Integer:
        return x + y


    @validated
    def pow(x: Integer, y: Integer) -> Integer:
        return x ** y


    print(add(3, 4))
    print(pow(2, 3))

    logged = logformat('{func.__code__.co_filename}:{func.__name__}')

    @logged
    def add(x,y):
        'Adds two things'
        return x+y

    a = add
    print(a)
    print(a.__name__)
    print(a.__doc__)
    a(2,2)


    class Spam:
        @logged
        def instance_method(self):
            pass

        @classmethod
        @logged
        def class_method(cls):
            pass

        @staticmethod
        @logged
        def static_method():
            pass

        @property
        @logged
        def property_method(self):
            pass

    s = Spam()
    s.instance_method()
    Spam.class_method()
    Spam.static_method()
    s.property_method
