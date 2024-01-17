import csv
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


def read_csv_as_dicts(filename, types):
    """
    Read a CSV file with column type conversion
    """
    parser = DictCSVParser(types)
    return parser.parse(filename)


def read_csv_as_instances(filename, cls):
    """
    Read a CSV file into a list of instances
    """
    parser = InstanceCSVParser(cls)
    return parser.parse(filename)


if __name__ == '__main__':
    portfolio = read_csv_as_dicts('Data/portfolio.csv', [str, int, float])
    print(portfolio)
    print(len(portfolio))
    print(portfolio[0])

    tracemalloc.start()
    parser = DictCSVParser([str, int, float])
    port = parser.parse('Data/portfolio.csv')
    print(tracemalloc.get_traced_memory())
