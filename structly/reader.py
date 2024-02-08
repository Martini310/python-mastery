import csv
from typing import List, Iterable
from abc import ABC, abstractmethod
import tracemalloc
import logging

log = logging.getLogger(__name__)
__all__ = ['read_csv_as_instances', 'read_csv_as_dicts']


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
# def read_csv_as_instances(filename, cls):
#     """
#     Read a CSV file into a list of instances
#     """
#     parser = InstanceCSVParser(cls)
#     return parser.parse(filename)

def read_csv_as_instances(filename, cls, *, headers=None):
    """
    Read CSV data into a list of instances
    """
    with open(filename) as file:
        return csv_as_instances(file, cls, headers=headers)


def read_csv_as_dicts(filename: str, types: List[object], headers: List[str] = None):
    """
    Read CSV data into a list of dictionaries with optional type conversion
    """
    with open(filename) as file:
        return csv_as_dicts(file, types, headers=headers)


def csv_as_instances(lines, cls, *, headers=None):
    return convert_csv(lines,
                       lambda headers, row: cls.from_row(row))


def csv_as_dicts(lines, types, *, headers=None):
    return convert_csv(lines,
                       lambda headers, row: {name: func(val) for name, func, val in zip(headers, types, row)})


def convert_csv(lines, converter, *, headers=None):
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for i, row in enumerate(rows, start=1):
        try:
            records.append(converter(headers, row))
        except ValueError as e:
            log.warning(f'Row {i}: Bad row: {row}')
            log.debug(f'Row {i}: Reason: {e}')
    return records
    # return list(map(lambda x: converter(headers, x), rows))


if __name__ == '__main__':
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


    def make_dict(headers, row):
        return dict(zip(headers, row))

    lines = open('Data/portfolio.csv')
    print(convert_csv(lines, make_dict))
    logging.basicConfig(level=logging.DEBUG)
    port = read_csv_as_dicts('Data/missing.csv', types=[str, int, float])
    print(len(port))



