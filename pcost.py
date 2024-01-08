
def portfolio_cost(filename):
    total_cost = 0
    with open(filename) as file:
        for line in file:
            fields = line.split()
            try:
                total_cost += int(fields[1]) * float(fields[2])
                
            except ValueError as e:
                print(f"Couldn't parse: {line}")
                print(f"Reason: {e}")

    return total_cost


if __name__ == '__main__':
    print(portfolio_cost('Data/portfolio3.dat'))
