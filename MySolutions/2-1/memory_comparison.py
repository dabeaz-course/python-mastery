import csv
import time
import tracemalloc
from collections import namedtuple
from io import TextIOWrapper

import pandas as pd
from loguru import logger

pd.options.plotting.backend = "plotly"


def read_into_string(f: TextIOWrapper):
    return f.read()


def read_into_lines(f: TextIOWrapper):
    return f.readlines()


def read_into_tuples(f: TextIOWrapper):
    records = []
    rows = csv.reader(f)
    next(rows)  # Skip headers
    for row in rows:
        route = row[0]
        date = row[1]
        daytype = row[2]
        rides = int(row[3])
        record = (route, date, daytype, rides)
        records.append(record)
    return records


def read_into_dictionary(f: TextIOWrapper):
    records = []
    rows = csv.reader(f)
    next(rows)  # Skip headers
    for row in rows:
        records.append(
            {"route": row[0], "date": row[1], "daytype": row[2], "rides": int(row[3])}
        )
    return records


def read_into_dictionary_with_pandas(f: TextIOWrapper):
    df = pd.DataFrame(f)
    return df.to_dict("records")


def read_into_named_tuple(f: TextIOWrapper):
    Row = namedtuple("Row", "route date daytype ride")
    records = []
    rows = csv.reader(f)
    next(rows)  # Skip headers
    for row in rows:
        records.append(Row(row[0], row[1], row[2], int(row[3])))
    return records


def read_into_class(f: TextIOWrapper):
    class Row:
        def __init__(self, route, date, daytype, rides):
            self.route = route
            self.date = date
            self.daytype = daytype
            self.rides = rides

    records = []
    rows = csv.reader(f)
    next(rows)  # Skip headers
    for row in rows:
        records.append(Row(row[0], row[1], row[2], int(row[3])))
    return records


def read_into_slot_class(f: TextIOWrapper):
    class Row:
        __slots__ = ["route", "date", "daytype", "rides"]

        def __init__(self, route, date, daytype, rides):
            self.route = route
            self.date = date
            self.daytype = daytype
            self.rides = rides

    records = []
    rows = csv.reader(f)
    next(rows)  # Skip headers
    for row in rows:
        records.append(Row(row[0], row[1], row[2], int(row[3])))
    return records


def read_into_dataframe(f: TextIOWrapper):
    return pd.DataFrame(f)


if __name__ == "__main__":
    all_methods = [
        read_into_string,
        read_into_lines,
        read_into_dictionary,
        read_into_dictionary_with_pandas,
        read_into_dataframe,
        read_into_tuples,
        read_into_named_tuple,
        read_into_class,
        read_into_slot_class,
    ]

    mem_usage_list = []

    with open("Data/ctabus.csv") as f:
        total_lines = len(f.readlines())

    for method in all_methods:
        start_time = time.time()
        tracemalloc.start()

        with open("Data/ctabus.csv") as f:
            data = method(f)
            current, peak = tracemalloc.get_traced_memory()
            current = round(current / 1000000, 2)
            peak = round(peak / 1000000, 2)
            logger.info(
                f"'{method.__name__}' Memory Usage - Current Memory: {current} MB | Peak Memory: {peak} MB"
            )

            mem_usage_list.append(
                {
                    "function_name": method.__name__,
                    "current_memory_MB": current,
                    "peak_memory_MB": peak,
                    "MB_per_record": current / total_lines,
                    "seconds_to_run": round(time.time() - start_time, 2),
                }
            )
        tracemalloc.stop()

    df = pd.DataFrame(mem_usage_list)
    print(df.head(len(all_methods)).sort_values("current_memory_MB"))
    fig = df.plot.scatter(
        title="Current vs Peak Memory Usage in MB",
        template="simple_white",
        x="current_memory_MB",
        y="peak_memory_MB",
        color="seconds_to_run",
        hover_data=["function_name"],
    )
    fig.show()
