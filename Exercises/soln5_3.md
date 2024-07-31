# Exercise 5.3 - Solution

## (a) Higher order functions

```python
# reader.py

import csv

def convert_csv(lines, converter, *, headers=None):
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = converter(headers, row)
        records.append(record)
    return records

def csv_as_dicts(lines, types, *, headers=None):
    return convert_csv(lines, 
                       lambda headers, row: { name: func(val) for name, func, val in zip(headers, types, row) })

def csv_as_instances(lines, cls, *, headers=None):
    return convert_csv(lines,
                       lambda headers, row: cls.from_row(row))

def read_csv_as_dicts(filename, types, *, headers=None):
    '''
    Read CSV data into a list of dictionaries with optional type conversion
    '''
    with open(filename) as file:
        return csv_as_dicts(file, types, headers=headers)

def read_csv_as_instances(filename, cls, *, headers=None):
    '''
    Read CSV data into a list of instances
    '''
    with open(filename) as file:
        return csv_as_instances(file, cls, headers=headers)
```

## (b) Using map()

```python
# reader.py

import csv

def convert_csv(lines, converter, *, headers=None):
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    return list(map(lambda row: converter(headers, row), rows))
```



[Back](ex5_3.md)
