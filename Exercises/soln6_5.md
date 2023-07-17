# Exercise 6.5 - Solution

```python
# validate.py
...

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
```



[Back](ex6_5.md)
