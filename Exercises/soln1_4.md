# Exercise 1.4 - Solution

## (a) Defining a function

```python
# pcost.py

def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename) as f:
        for line in f:
            fields = line.split()
            nshares = int(fields[1])
            price = float(fields[2])
            total_cost = total_cost + nshares * price
    return total_cost

print(portfolio_cost('Data/portfolio.dat'))
```

## (b) Adding some error handling

```python
# pcost.py

def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename) as f:
        for line in f:
            fields = line.split()
            try:
                nshares = int(fields[1])
                price = float(fields[2])
                total_cost = total_cost + nshares*price

            # This catches errors in int() and float() conversions above
            except ValueError as e:
                print("Couldn't parse:", repr(line))
                print("Reason:", e)
    return total_cost

print(portfolio_cost('Data/portfolio3.dat'))
```


[Back](ex1_4.md)
