# colreader.py

import collections
import csv

class DataCollection(collections.abc.Sequence):
    def __init__(self, columns):
        self.column_names = list(columns)
        self.column_data = list(columns.values())

    def __len__(self):
        return len(self.column_data[0])

    def __getitem__(self, index):
        return dict(zip(self.column_names,
                        (col[index] for col in self.column_data)))


def read_csv_as_columns(filename, types):
    columns = collections.defaultdict(list)
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            for name, func, val in zip(headers, types, row):
                columns[name].append(func(val))
            
    return DataCollection(columns)

if __name__ == '__main__':
    import tracemalloc
    from sys import intern

    tracemalloc.start()
    data = read_csv_as_columns('../../Data/ctabus.csv', [intern, intern, intern, int])
    print(tracemalloc.get_traced_memory())
