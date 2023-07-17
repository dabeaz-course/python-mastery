
# Exercise 3.7 - Solution

## (a) Interfaces

```python
# tableformat.py

def print_table(records, fields, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError('Expected a TableFormatter')

    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)
...
```

## (b) Abstract Base Classes

```python
# tableformat.py
from abc import ABC, abstractmethod

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass
```

## (c) Algorithm Template Classes

```python
# reader.py

import csv
from abc import ABC, abstractmethod

class CSVParser(ABC):
    def parse(self, filename):
        records = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                record = self.make_record(headers, row)
                records.append(record)
        return records

    @abstractmethod
    def make_record(self, headers, row):
        pass

class DictCSVParser(CSVParser):
    def __init__(self, types):
        self.types = types

    def make_record(self, headers, row):
        return { name: func(val) for name, func, val in zip(headers, self.types, row) }

class InstanceCSVParser(CSVParser):
    def __init__(self, cls):
        self.cls = cls

    def make_record(self, headers, row):
        return self.cls.from_row(row)

def read_csv_as_dicts(filename, types):
    parser = DictCSVParser(types)
    return parser.parse(filename)

def read_csv_as_instances(filename, cls):
    parser = InstanceCSVParser(cls)
    return parser.parse(filename)
```




[Back](ex3_7.md)
