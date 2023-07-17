# Exercise 2.4 - Solution

```python
# mutint.py

from functools import total_ordering

@total_ordering
class MutInt:
    __slots__ = ['value']

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return f'MutInt({self.value!r})'

    def __format__(self, fmt):
        return format(self.value, fmt)

    # Implement the "+" operator. Forward operands (MutInt + other)
    def __add__(self, other):
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented

    # Support for reversed operands (other + MutInt)
    __radd__ = __add__

    # Support for in-place update (MutInt += other)
    def __iadd__(self, other):
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented

    # Support for equality testing
    def __eq__(self, other):
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    # One relation is needed for @total_ordering decorator. It fills in others
    def __lt__(self, other):
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented

    # Conversions to int() and float()
    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    # Support for indexing s[MutInt]
    __index__ = __int__
```



[Back](ex2_4.md)
