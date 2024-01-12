import csv
from collections import abc
import tracemalloc
from sys import intern


def read_csv_as_dicts(filename, coltypes):
    """
    Read a CSV file with column type conversion
    """
    records = []
    with open(filename) as f:
        file = csv.reader(f)
        headers = next(file)
        for row in file:
            records.append({name: func(val) for name, func, val in zip(headers, coltypes, row)})
        return records


def read_csv_as_columns(filename, types=None):
    with open(filename) as f:
        file = csv.reader(f)
        headers = next(file)
        records = DataCollection(headers)
        for line in file:
            records.append({name: func(val) for name, val, func in zip(headers, line, types)})
        return records


def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
    return records


class DataCollection(abc.Sequence):
    def __init__(self, colnames):
        self.colnames = colnames
        for name in colnames:
            setattr(self, name, [])

    def __len__(self):
        col = getattr(self, self.colnames[0], [])
        return len(col)

    def __getitem__(self, item):
        return {
            attr: getattr(self, attr)[item] for attr in self.colnames
        }

    def append(self, d):
        for key, value in d.items():
            getattr(self, key).append(value)


if __name__ == '__main__':

    portfolio = read_csv_as_columns('Data/portfolio.csv', [str,int,float])
    print(portfolio)
    print(len(portfolio))
    print(portfolio[0])

    tracemalloc.start()
    data = read_csv_as_columns('Data/ctabus.csv', types=[intern, intern, intern, int])
    print(data)
    print(len(data))
    print(data[0])
    print(data[1])
    print(tracemalloc.get_traced_memory())
