# Exercise 3.2 - Solution

(c) Table Formatter

```python
# tableformat.py

# Print a table
def print_table(records, fields):
    print(' '.join('%10s' % fieldname for fieldname in fields))
    print(('-'*10 + ' ')*len(fields))
    for record in records:
        print(' '.join('%10s' % getattr(record, fieldname) for fieldname in fields))
```



[Back](ex3_2.md)
