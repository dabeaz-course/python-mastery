import csv
import sys


def read_rides_as_tupples(filename):
    """Read the bus ride data as a list of tupples"""
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
        return records


def read_rides_as_dicts(filename):
    """Read the bus ride data as a list of dicts"""
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {"route": route, "date": date, "daytype": daytype, "rides": rides}
            records.append(record)
        return records


def read_rides_as_objects(filename):
    """Read the bus ride data as a list of objects"""

    class Row:
        def __init__(self, route, date, daytype, rides):
            self.route = route
            self.date = date
            self.daytype = daytype
            self.rides = rides

    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides)
            records.append(record)
        return records


def read_rides_as_named_tuples(filename):
    """Read the bus ride data as a list of named tuples"""
    # from collections import namedtuple

    # Row = namedtuple("Row", ["route", "date", "daytype", "rides"])
    import typing

    class Row(typing.NamedTuple):
        route: str
        date: str
        daytype: str
        rides: int

    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides)
            records.append(record)
        return records


def read_rides_as_slot_objects(filename):
    """Read the bus ride data as a list of slot objects"""

    class Row:
        __slots__ = ("route", "date", "daytype", "rides")

        def __init__(self, route, date, daytype, rides):
            self.route = route
            self.date = date
            self.daytype = daytype
            self.rides = rides

    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides)
            records.append(record)
        return records


if __name__ == "__main__":
    import tracemalloc

    tracemalloc.start()
    if sys.argv[1] == "tuple":
        rows = read_rides_as_tupples("Data/ctabus.csv")
    elif sys.argv[1] == "dict":
        rows = read_rides_as_dicts("Data/ctabus.csv")
    elif sys.argv[1] == "obj":
        rows = read_rides_as_objects("Data/ctabus.csv")
    elif sys.argv[1] == "namedtuple":
        rows = read_rides_as_named_tuples("Data/ctabus.csv")
    elif sys.argv[1] == "slot":
        rows = read_rides_as_slot_objects("Data/ctabus.csv")

    print("Memory Use: Current %d, Peak %d" % tracemalloc.get_traced_memory())
