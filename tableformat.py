from stock import read_portfolio, Stock


def print_table(list_of_obj, attr_names):
    print(''.join(f'{name:>10}' for name in attr_names))
    print(f'{("-" * 10 + " ") * len(attr_names)}')
    for obj in list_of_obj:
        print(''.join(f"{getattr(obj, name):>10}" for name in attr_names))


if __name__ == '__main__':
    portfolio = read_portfolio('Data/portfolio.csv', Stock)
    print_table(portfolio, ['name', 'shares', 'price'])
    print_table(portfolio, ['shares', 'name'])
