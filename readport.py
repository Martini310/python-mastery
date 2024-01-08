import csv
from collections import Counter, defaultdict
from readrides import read_rides_as_slots_classes

# A function that reads a file into a list of dicts
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(record)
    return portfolio


# Task 1
# with open('Data/ctabus.csv') as f:
#     rows = csv.reader(f)
#     header = next(rows)
#     routes = defaultdict(list)
#     for r in rows:
#         routes['routes'].append(r[0])
#
# print(len(set(routes['routes'])))


# Task 2
# def people_by_route(number, date):
#     rows = read_rides_as_slots_classes('Data/ctabus.csv')
#     for row in rows:
#         if row.route == str(number) and row.date == date:
#             print(row.rides)
#
#
# people_by_route(22, '02/02/2011')


# Task 3
# with open('Data/ctabus.csv') as f:
#     rows = csv.reader(f)
#     header = next(rows)
#     total = Counter()
#     for r in rows:
#         total[r[0]] += int(r[3])
#
# print(total)


# Task 4
with open('Data/ctabus.csv') as f:
    rows = csv.reader(f)
    header = next(rows)
    people_by_year = dict()
    for r in rows:
        people_by_year[r[0]] = {}
    for k in people_by_year:
        people_by_year[k] = Counter()

with open('Data/ctabus.csv') as f:
    rows = csv.reader(f)
    header = next(rows)
    for r in rows:
        number = r[0]
        year = r[1][-4:]
        people_by_year[number][year] += int(r[3])

print(people_by_year)
