"""
import random

for x in range(5):
    c = random.randint(1,50)

    print(c)

"""

###  ITERTOOL
"""
from itertools import count

for i in count(3):
    print(i)
    if i>=20:
        break
"""
"""
from itertools import accumulate

number=list(accumulate(range(8)))

print(number)

"""

from itertools import accumulate,takewhile

number=list(accumulate(range(8)))

print(number)
print(list(takewhile(lambda x : x<10 ,number)))