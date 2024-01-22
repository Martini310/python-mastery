import csv
from typing import List, Iterable
from abc import ABC, abstractmethod
import tracemalloc


class CSVParser(ABC):

    def parse(self, filename):
        records = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                record = self.make_record(headers, row)
                records.append(record)
        return records

    @abstractmethod
    def make_record(self, headers, row):
        pass


class DictCSVParser(CSVParser):
    def __init__(self, types):
        self.types = types

    def make_record(self, headers, row):
        return {name: func(val) for name, func, val in zip(headers, self.types, row)}


class InstanceCSVParser(CSVParser):
    def __init__(self, cls):
        self.cls = cls

    def make_record(self, headers, row):
        return self.cls.from_row(row)


# def read_csv_as_dicts(filename, types):
#     """
#     Read a CSV file with column type conversion
#     """
#     parser = DictCSVParser(types)
#     return parser.parse(filename)
#
#
def read_csv_as_instances(filename, cls):
    """
    Read a CSV file into a list of instances
    """
    parser = InstanceCSVParser(cls)
    return parser.parse(filename)


def read_csv_as_dicts(filename: str, types: List[object], headers: List[str] = None):
    '''
    Read CSV data into a list of dictionaries with optional type conversion
    '''
    with open(filename) as file:
        csv_as_dicts(file, types, headers)


def csv_as_dicts(lines: Iterable, types: List[object], headers: List[str] = None) -> List[dict]:
    '''
    Convert lines of CSV data into a list of dictionaries
    '''
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = { name: func(val)
                   for name, func, val in zip(headers, types, row) }
        records.append(record)
    return records


def csv_as_instances(lines, cls):
    '''
    Convert lines of CSV data into a list of instances
    '''
    records = []
    rows = csv.reader(lines)
    headers = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records


if __name__ == '__main__':
    # portfolio = read_csv_as_dicts('Data/portfolio.csv', [str, int, float])
    # print(portfolio)
    # print(len(portfolio))
    # print(portfolio[0])
    #
    # import stock
    # port = read_csv_as_instances('Data/portfolio.csv', stock.Stock)
    # print(port)
    # tracemalloc.start()
    # parser = DictCSVParser([str, int, float])
    # port = parser.parse('Data/portfolio.csv')
    # print(tracemalloc.get_traced_memory())

    file = open('Data/portfolio.csv')
    port = csv_as_dicts(file, [str, int, float])
    print(port)

    import gzip
    import stock
    file = gzip.open('Data/portfolio.csv.gz', 'rt')
    port = csv_as_instances(file, stock.Stock)
    print(port)
