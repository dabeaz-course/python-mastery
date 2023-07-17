# Exercise 6.1 - Solution

## (a) Simplified Structures

```python
# structure.py

class Structure:
    _fields = ()
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected %d arguments' % len(self._fields))
        for name, arg in zip(self._fields,args):
            setattr(self, name, arg)
```

## (b) Making a Useful Representation

[source, python]
```
class Structure:
    ...    
    def __repr__(self):
        return '%s(%s)' % (type(self).__name__,
                           ', '.join(repr(getattr(self, name)) for name in self._fields))
```

## (c) Restricting Attribute Names

[source, python]
```
class Structure:
    ...    
    def __setattr__(self, name, value):
        if name.startswith('_') or name in self._fields:
            super().__setattr__(name, value)
        else:
            raise AttributeError('No attribute %s' % name)
```



[Back](ex6_1.md)
