# reader.py

from abc import ABC, abstractmethod
import csv
import logging
log = logging.getLogger(__name__)

class CSVParser(ABC):

    def parse(self, filename):
        records = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for rowno, row in enumerate(rows, start=1):
                try:
                    record = self.make_record(headers, row)
                    records.append(record)
                except ValueError as e:
                    log.warning('Row %d: Bad row: %s', rowno, row)
                    log.debug('Row %d: Reason: %s', rowno, e)

        return records

    @abstractmethod
    def make_record(self, headers, row):
        raise NotImplementedError()

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
