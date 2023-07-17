# Exercise 8.6 - Solution

## (a) Receiving Messages

```python
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
    follow('Data/stocklog.csv',
           to_csv(
           create_ticker(
           negchange(
           ticker('text', ['name','price','change'])))))
```

## (b) Wrapping a Socket

```python
# server.py
...

class GenSocket:
    def __init__(self, sock):
        self.sock = sock

    def accept(self):
        yield 'recv', self.sock
        client, addr = self.sock.accept()
        return GenSocket(client), addr

    def recv(self, maxsize):
        yield 'recv', self.sock
        return self.sock.recv(maxsize)

    def send(self, data):
        yield 'send', self.sock
        return self.sock.send(data)

    def __getattr__(self, name):
        return getattr(self.sock, name)

def tcp_server(address, handler):
    sock = GenSocket(socket(AF_INET, SOCK_STREAM))
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        client, addr = yield from sock.accept()
        tasks.append(handler(client, addr))
        
def echo_handler(client, address):
    print('Connection from', address)
    while True:
        data = yield from client.recv(1000)
        if not data:
            break
        yield from client.send(b'GOT:' + data)
    print('Connection closed')

if __name__ == '__main__':
    tasks.append(tcp_server(('',25000), echo_handler))
    run()
```

## (c) Async/Await

```python
# server.py

from socket import *
from select import select
from collections import deque
from types import coroutine

tasks = deque()
recv_wait = {}   #  sock -> task
send_wait = {}   #  sock -> task

def run():
    while any([tasks, recv_wait, send_wait]):
        while not tasks:
            can_recv, can_send, _ = select(recv_wait, send_wait, [])
            for s in can_recv:
                tasks.append(recv_wait.pop(s))
            for s in can_send:
                tasks.append(send_wait.pop(s))
        task = tasks.popleft()
        try:
            reason, resource = task.send(None)
            if reason == 'recv':
                recv_wait[resource] = task
            elif reason == 'send':
                send_wait[resource] = task
            else:
                raise RuntimeError('Unknown reason %r' % reason)
        except StopIteration:
            print('Task done')

class GenSocket:
    def __init__(self, sock):
        self.sock = sock

    @coroutine
    def accept(self):
        yield 'recv', self.sock
        client, addr = self.sock.accept()
        return GenSocket(client), addr

    @coroutine
    def recv(self, maxsize):
        yield 'recv', self.sock
        return self.sock.recv(maxsize)

    @coroutine
    def send(self, data):
        yield 'send', self.sock
        return self.sock.send(data)

    def __getattr__(self, name):
        return getattr(self.sock, name)

async def tcp_server(address, handler):
    sock = GenSocket(socket(AF_INET, SOCK_STREAM))
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    while True:
        client, addr = await sock.accept()
        tasks.append(handler(client, addr))
        
async def echo_handler(client, address):
    print('Connection from', address)
    while True:
        data = await client.recv(1000)
        if not data:
            break
        await client.send(b'GOT:' + data)
    print('Connection closed')

if __name__ == '__main__':
    tasks.append(tcp_server(('',25000), echo_handler))
    run()
```



[Back](ex8_6.md)
