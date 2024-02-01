def portfolio_cost(filename):
    cost = 0.0
    with open(filename) as lines:
        for line in lines:
            _, shares, price = line.split()
            try:
                cost += int(shares) * float(price)
            except ValueError as e:
                print(f"Couldn't parse: {line}")
                print(f"Reason: {e}")
    return cost


if __name__ == "__main__":
    print(portfolio_cost("Data/portfolio3.dat"))
