# Exercise 6.3 - Solution

```python
# structure.py

import sys
import inspect

class Structure:
    _fields = ()

    @staticmethod
    def _init():
        locs = sys._getframe(1).f_locals
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)

    def __setattr__(self, name, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError('No attribute %s' % name)

    def __repr__(self):
        return '%s(%s)' % (type(self).__name__,
                           ', '.join(repr(getattr(self, name)) for name in self._fields))

    @classmethod
    def set_fields(cls):
        sig = inspect.signature(cls)
        cls._fields = tuple(sig.parameters)
```

Here is the `Stock` class in progress:

```python
# stock.py

from structure import Structure

class Stock(Structure):
    def __init__(self, name, shares, price):
        self._init()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

Stock.set_fields()
```



[Back](ex6_3.md)
