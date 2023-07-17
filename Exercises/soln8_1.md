# Exercise 8.1 - Solution

## (b) Adding Iteration to Objects

```python
# structure.py
...
        
class Structure(metaclass=StructureMeta):
    ...
    def __iter__(self):
        for name in self._fields:
            yield getattr(self, name)
    ...
```

## (c) The Surprising Power of Iteration

```python
# structure.py
...
        
class Structure(metaclass=StructureMeta):
    ...
    def __eq__(self, other):
        return isinstance(other, type(self)) and tuple(self) == tuple(other)
    ...
```

## (d) Monitoring a streaming data source

```python
# follow.py
import os
import time

def follow(filename):
    '''
    Generator that produces a sequence of lines being written at the end of a file.
    '''
    with open(filename,'r') as f:
        f.seek(0,os.SEEK_END)
        while True:
             line = f.readline()
             if line == '':
                 time.sleep(0.1)    # Sleep briefly to avoid busy wait
                 continue
             yield line

# Example use
if __name__ == '__main__':
    for line in follow('Data/stocklog.csv'):
        row = line.split(',')
        name = row[0].strip('"')
        price = float(row[1])
        change = float(row[4])
        if change < 0:
            print('%10s %10.2f %10.2f' % (name, price, change))
```

**Discussion**

The `time.sleep()` function is being used here to avoid busy-waiting
on the CPU (e.g., sitting in an infinite loop with 100% CPU use while waiting for new lines to arrive)



[Back](ex8_1.md)
