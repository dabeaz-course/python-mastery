# Exercise 9.2 - Solution

## (a) Making a package

You don't need to modify much source code.   Just make a directory with
this structure:

```
structly/
    __init__.py
    validate.py
    reader.py
    structure.py
    tableformat.py
```

The `__init__.py` file can be empty.  You need to make one small change to the `structure.py` file to make the import statement work.

```python
# structure.py

...
from .validate import Validator
```



[Back](ex9_2.md)
