# coticker.py
from structure import Structure
from validate import String, Integer, Float

class Ticker(Structure):
    name = String()
    price = Float()
    date = String()
    time = String()
    change = Float()
    open = Float()
    high = Float()
    low = Float()
    volume = Integer()

from cofollow import consumer, follow, receive
from tableformat import create_formatter
import csv

@consumer
def to_csv(target):
    def producer():
        while True:
            yield line

    reader = csv.reader(producer())
    while True:
        line = yield from receive(str)
        target.send(next(reader))

@consumer
def create_ticker(target):
    while True:
        row = yield from receive(list)
        target.send(Ticker.from_row(row))

@consumer
def negchange(target):
    while True:
        record = yield from receive(Ticker)
        if record.change < 0:
            target.send(record)

@consumer
def ticker(fmt, fields):
    formatter = create_formatter('text')
    formatter.headings(fields)
    while True:
        rec = yield from receive(Ticker)
        row = [getattr(rec, name) for name in fields]
        formatter.row(row)

if __name__ == '__main__':
    follow('../../Data/stocklog.csv',
           to_csv(
           create_ticker(
           negchange(
           ticker('text', ['name','price','change'])))))
