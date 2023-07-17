# validate.py

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
from functools import wraps

def isvalidator(item):
    return isinstance(item, type) and issubclass(item, Validator)

def validated(func):
    sig = signature(func)

    # Gather the function annotations
    annotations = { name:val for name, val in func.__annotations__.items()
                    if isvalidator(val) }

    # Get the return annotation (if any)
    retcheck = annotations.pop('return', None)

    @wraps(func)
    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs)
        errors = []

        # Enforce argument checks
        for name, validator in annotations.items():
            try:
                validator.check(bound.arguments[name])
            except Exception as e:
                errors.append(f'  {name}: {e}')

        if errors:
            raise TypeError('Bad Arguments\n' + '\n'.join(errors))

        result = func(*args, **kwargs)

        # Enforce return check (if any)
        if retcheck:
            try:
                retcheck.check(result)
            except Exception as e:
                raise TypeError(f'Bad return: {e}') from None
        return result

    return wrapper

def enforce(**annotations):
    retcheck = annotations.pop('return_', None)

    def decorate(func):
        sig = signature(func)

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound = sig.bind(*args, **kwargs)
            errors = []

            # Enforce argument checks
            for name, validator in annotations.items():
                try:
                    validator.check(bound.arguments[name])
                except Exception as e:
                    errors.append(f'    {name}: {e}')

            if errors:
                raise TypeError('Bad Arguments\n' + '\n'.join(errors))

            result = func(*args, **kwargs)

            if retcheck:
                try:
                    retcheck.check(result)
                except Exception as e:
                    raise TypeError(f'Bad return: {e}') from None
            return result
        return wrapper
    return decorate

# Examples
if __name__ == '__main__':
    @validated
    def add(x:Integer, y:Integer) -> Integer:
        return x + y

    @validated
    def div(x:Integer, y:Integer) -> Integer:
        return x / y

    @enforce(x=Integer, y=Integer)
    def sub(x, y):
        return x - y

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

        @validated
        def sell(self, nshares:PositiveInteger):
            self.shares -= nshares

    

    
