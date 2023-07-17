class Validator:
    def __init__(self, name=None):
        self.name = name

    def __set_name__(self, cls, name):
        self.name = name

    @classmethod
    def check(cls, value):
        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)

class Typed(Validator):
    expected_type = object
    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'expected {cls.expected_type}')
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
            raise ValueError('must be >= 0')
        return super().check(value)

class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if len(value) == 0:
            raise ValueError('must be non-empty')
        return super().check(value)

class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

class NonEmptyString(String, NonEmpty):
    pass

from inspect import signature

class ValidatedFunction:
    def __init__(self, func):
        self.func = func
        self.signature = signature(func)
        self.annotations = dict(func.__annotations__)
        self.retcheck = self.annotations.pop('return', None)

    def __call__(self, *args, **kwargs):
        bound = self.signature.bind(*args, **kwargs)

        for name, val in self.annotations.items():
            val.check(bound.arguments[name])

        result = self.func(*args, **kwargs)

        if self.retcheck:
            self.retcheck.check(result)

        return result

# Examples
if __name__ == '__main__':
    def add(x:Integer, y:Integer) -> Integer:
        return x + y

    add = ValidatedFunction(add)

    class Stock:
        name = NonEmptyString()
        shares = PositiveInteger()
        price = PositiveFloat()
        def __init__(self, name, shares, price):
            self.name = name
            self.shares = shares
            self.price = price

        def __repr__(self):
            return f'Stock({self.name!r}, {self.shares!r}, {self.price!r})'

        @property
        def cost(self):
            return self.shares * self.price

        def sell(self, nshares):
            self.shares -= nshares

        sell = ValidatedFunction(sell)     # Broken



    

    
