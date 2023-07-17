# pcost.py

total_cost = 0.0

with open('../../Data/portfolio.dat', 'r') as f:
    for line in f:
        fields = line.split()
        nshares = int(fields[1])
        price = float(fields[2])
        total_cost = total_cost + nshares * price

print(total_cost)
