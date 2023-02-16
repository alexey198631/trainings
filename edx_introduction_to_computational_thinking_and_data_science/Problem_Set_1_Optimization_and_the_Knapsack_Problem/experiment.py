from ps1 import *

def greedy_cow_transport(cows,limit=10):

    pass


values = []
max = 0
for v in cows.values():
    if v > max:
        max = v

print(max)

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k


print(get_key(cows, max))


