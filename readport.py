import csv
import tracemalloc
from collections import Counter, defaultdict
from readrides import read_rides_as_slots_classes


# A function that reads a file into a list of dicts
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        lines = csv.reader(f)
        headers = next(lines)
        for line in lines:
            record = {
                'name': line[0],
                'shares': int(line[1]),
                'price': float(line[2])
            }
            portfolio.append(record)
    return portfolio


tracemalloc.start()

rows = read_rides_as_slots_classes('Data/ctabus.csv')

# Task 1  How many bus routes are in Chicago?
routes = []
for r in rows:
    routes.append(r.route)
print('Task 1', len(set(routes)))


# Task 2  How many people rode route 22 on February 2, 2011?
by_route_date = {}
for row in rows:
    by_route_date[row.route, row.date] = row.rides


def people_by_route(bus_num, date):
    return by_route_date[str(bus_num), date]


print('Task 2', people_by_route(22, '02/02/2011'))


# Task 3  Total number of rides per route
total = Counter()
for r in rows:
    total[r.route] += int(r.rides)

print('Task 3')
for route, count in total.most_common(5):
    print(f"{route:>8} {count:10}")
print('----------------------------')


# Task 4  Routes with the greatest increase in ridership 2001 - 2011
rides_by_year = defaultdict(Counter)
for r in rows:
    year = r.date.split('/')[2]
    rides_by_year[year][r.route] += r.rides

diffs = rides_by_year['2011'] - rides_by_year['2001']
print('Task 4')
for route, rides in diffs.most_common(5):
    print(f'Route: {route:>4} - {rides:7} rides more')


print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
