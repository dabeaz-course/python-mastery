# reader.py

import csv

def read_csv_as_dicts(filename, types):
    '''
    Read a CSV file into a list of dicts with column type conversion
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = { name: func(val) for name, func, val in zip(headers, types, row) }
            records.append(record)
    return records

        

    


