# Exercise 9.3 - Solution

## (a) Controlling Exported Symbols

```python
# structure.py

__all__ = ['Structure']
...
```

```python
# reader.py

__all__ = [ 'read_csv_as_dicts',
            'read_csv_as_instances' ]
...
```

```python
# tableformat.py

__all__ = ['create_formatter', 'print_table']
...
```

## (b) Exporting Everything

```python
# structly/__init__.py

from .structure import *
from .reader import *
from .tableformat import *

__all__ = [ *structure.__all__,
	    *reader.__all__,
	    *tableformat.__all__ ]
```

## (c) Module Splitting

There are a few parts to this.   First, the individual files in `tableformat/formats` are going to
look like this:

```python
# tableformat/formats/text.py
from ..formatter import TableFormatter

class TextTableFormatter(TableFormatter):
    ...


# tableformat/formats/csv.py
from ..formatter import TableFormatter
class CSVTableFormatter(TableFormatter):
    ...


# tableformat/formats/html.py
from ..formatter import TableFormatter
class HTMLTableFormatter(TableFormatter):
    ...
```

The `formatter.py` file will look like this:

```python
# tableformat/formatter.py

from abc import ABC, abstractmethod

def print_table(records, fields, formatter):
    if not isinstance(formatter, TableFormatter):
        raise RuntimeError('Expected a TableFormatter')

    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass

from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter

class ColumnFormatMixin:
    formats = []
    def row(self, rowdata):
        rowdata = [ (fmt % item) for fmt, item in zip(self.formats, rowdata)]
        super().row(rowdata)

class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])

def create_formatter(name, column_formats=None, upper_headers=False):
    if name == 'text':
        formatter_cls = TextTableFormatter
    elif name == 'csv':
        formatter_cls = CSVTableFormatter
    elif name == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError('Unknown format %s' % name)

    if column_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
              formats = column_formats

    if upper_headers:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass

    return formatter_cls()
```

Finally, you need to have a `tableformat/__init__.py` file like this:

```python
# tableformat/__init__.py

from .formatter import print_table, create_formatter

__all__ = [ 'print_table', 'create_formatter' ]
```


[Back](ex9_3.md)
