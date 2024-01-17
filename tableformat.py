from stock import read_portfolio, Stock
import reader
from abc import ABC, abstractmethod


# def print_table(list_of_obj, attr_names):
#     print(''.join(f'{name:>10}' for name in attr_names))
#     print(f'{("-" * 10 + " ") * len(attr_names)}')
#     for obj in list_of_obj:
#         print(''.join(f"{getattr(obj, name):>10}" for name in attr_names))
def print_table(records, fields, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError("Expected a TableFormatter")

    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)


class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-' * 10 + ' ') * len(headers))

    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(str(row) for row in rowdata))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', end='')
        for header in headers:
            print(f'<th>{header}</th>', end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for r in rowdata:
            print(f'<td>{r}</td>', end='')
        print('</tr>')


def create_formatter(name):
    if name == 'text':
        formatter_cls = TextTableFormatter
    elif name == 'csv':
        formatter_cls = CSVTableFormatter
    elif name == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError('Unknown format %s' % name)
    return formatter_cls()


if __name__ == '__main__':
    portfolio = reader.read_csv_as_instances('Data/portfolio.csv', Stock)
    formatter = create_formatter('csv')
    print_table(portfolio, ['name', 'shares', 'price'], formatter)
