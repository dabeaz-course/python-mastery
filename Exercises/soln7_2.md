# Exercise 7.2 - Solution

## (a) Copying Metadata

```python
# logcall.py

from functools import wraps

def logged(func):
    print('Adding logging to', func.__name__)
    @wraps(func)
    def wrapper(*args,**kwargs):
        print('Calling', func.__name__)
        return func(*args,**kwargs)
    return wrapper
```

## (b) Decorators with arguments

```python
# logcall.py

from functools import wraps
...
def logformat(fmt):
    def logged(func):
        print('Adding logging to', func.__name__)
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(fmt.format(func=func))
            return func(*args, **kwargs)
        return wrapper
    return logged
```

The earlier `@logged` decorator can be rewritten as follows:

```python
logged = logformat('Calling {func.__name__}')
```

## (c) Decorators and methods

You can get the code to work if you interchange the order of the 
decorators.  For example:

```python
from logcall import logged

class Spam:
    @logged
    def instance_method(self):
        pass

    @classmethod
    @logged
    def class_method(cls):
        pass

    @staticmethod
    @logged
    def static_method():
        pass

    @property
    @logged
    def property_method(self):
        pass
```

Ponder why it doesn't work in the original order.  Is there any way to make
the `@logged` decorator work regardless of the order in which its applied?

## (d) Validation (Redux)

```python
# validate.py
...

from inspect import signature
from functools import wraps

def validated(func):
    sig = signature(func)

    # Gather the function annotations
    annotations = dict(func.__annotations__)

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
                errors.append(f'    {name}: {e}')

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
```




[Back](ex7_2.md)
