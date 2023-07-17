# Exercise 3.6 - Solution

## (a) Better output for printing objects

```python
# stock.py

class Stock:
    ...

    def __repr__(self):
        # Note: The !r format code produces the repr() string
        return f'{type(self).__name__}({self.name!r}, {self.shares!r}, {self.price!r})'
    ...
```

## (b) Making Objects Comparable

```python
class Stock:
    ...
    def __eq__(self, other):
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) ==
                                 (other.name, other.shares, other.price))
    ...
```

## (c) Context Managers

Code is given in the exercise.



[Back](ex3_6.md)
