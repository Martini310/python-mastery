def logged(func):
    print('Adding logging to', func.__name__)

    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper


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
    print(pow(2, -3))

