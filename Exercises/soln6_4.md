# Exercise 6.4 - Solution

```python
# structure.py

class Structure:
    _fields = ()

    def __setattr__(self, name, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError('No attribute %s' % name)

    def __repr__(self):
        return '%s(%s)' % (type(self).__name__,
                           ', '.join(repr(getattr(self, name)) for name in self._fields))

    @classmethod
    def create_init(cls):
        args = ','.join(cls._fields)
        code = 'def __init__(self, {0}):\n'.format(args)
        statements = [ '    self.{0} = {0}'.format(name) for name in cls._fields]
        code += '\n'.join(statements)
        locs = { }
        exec(code, locs)
        cls.__init__ = locs['__init__']
```

Here is the `Stock` class in progress after this change:

```python
# stock.py

from structure import Structure

class Stock(Structure):
    _fields = ('name', 'shares', 'price')

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

Stock.create_init()
```



[Back](ex6_4.md)
