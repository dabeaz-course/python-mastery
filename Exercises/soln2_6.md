# Exercise 2.6 - Solution

```python
# reader.py

import csv
from collections import defaultdict

def read_csv_as_dicts(filename, types):
    '''
    Read a CSV file with column type conversion
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = { name: func(val) for name, func, val in zip(headers, types, row) }
            records.append(record)
    return records
```



[Back](ex2_6.md)
