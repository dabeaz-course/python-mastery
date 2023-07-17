# follow.py
import os
import time

def follow(filename):
    '''
    Generator that produces a sequence of lines being written at the end of a file.
    '''
    try:
        with open(filename,'r') as f:
            f.seek(0,os.SEEK_END)
            while True:
                 line = f.readline()
                 if line == '':
                     time.sleep(0.1)    # Sleep briefly to avoid busy wait
                     continue
                 yield line
    except GeneratorExit:
        print('Following Done')

def splitter(lines):
    for line in lines:
        yield line.split(',')


def make_records(rows,names):
    for row in rows:
        yield dict(zip(names,row))

def unquote(records,keylist):
    for r in records:
        for key in keylist:
            r[key] = r[key].strip('"')
        yield r

def convert(records,converter,keylist):
    for r in records:
        for key in keylist:
            r[key] = converter(r[key])
        yield r

def parse_stock_data(lines):
    rows = splitter(lines)
    records = make_records(rows,['name','price','date','time',
                              'change','open','high','low','volume'])
    records = unquote(records,["name","date","time"])
    records = convert(records,float,['price','change','open','high','low'])
    records = convert(records,int,['volume'])
    return records

# Sample use
if __name__ == '__main__':
   lines = follow("../../Data/stocklog.dat")
   records = parse_stock_data(lines)
   for r in records:
       print("%(name)10s %(price)10.2f %(change)10.2f" % r)
