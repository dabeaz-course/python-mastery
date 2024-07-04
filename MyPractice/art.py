import sys
import random

chars='\|/'

def draw(rows,column):

    for r in range(rows):
        print(''.join(random.choice(chars) for c in range(column)))


draw(10, 20)


