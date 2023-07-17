# Exercise 4.2 - Solution

Here is the validator code in its entirety:

```python
class Validator:
    @classmethod
    def check(cls, value):
        return value

class Typed(Validator):
    expected_type = object
    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return super().check(value)

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str

class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value < 0:
            raise ValueError('Must be >= 0')
        return super().check(value)

class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if len(value) == 0:
            raise ValueError('Must be non-empty')
        return super().check(value)

class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

class NonEmptyString(String, NonEmpty):
    pass
```

## (c) Using the validators

```python
# validate.py
...

if __name__ == '__main__':
    class Stock:
        __slots__ = ('name', '_shares', '_price')
        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price

        def __repr__(self):
            return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'

        @property
        def shares(self):
            return self._shares
        @shares.setter
        def shares(self, value):
            self._shares = PositiveInteger.check(value)

        @property
        def price(self):
            return self._price
        @price.setter
        def price(self, value):
            self._price = PositiveFloat.check(value)

        @property
        def cost(self):
            return self.shares * self.price

        def sell(self, nshares):
            self.shares -= nshares
```



[Back](ex4_2.md)
