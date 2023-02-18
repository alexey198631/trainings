"""
Write a Python function that returns a list of keys in aDict that map to integer values that are unique
(i.e. values appear exactly once in aDict).
The list of keys you return should be sorted in increasing order.
(If aDict does not contain any unique values, you should return an empty list.)

This function takes in a dictionary and returns a list.
"""


# creating list of all values from the dictionary - > list
def lst(aDict):
    val = []
    for v in aDict.values():
        val.append(v)
    return val


# counting values - > dict
def ulistcount(lst):
    counts = dict()
    for n in lst:
        counts[n] = counts.get(n, 0) + 1
    return counts


# unique values - > list
def unique(ulistcount):
    ulst = []
    for k in ulistcount:
        if ulistcount[k] == 1:
            ulst.append(k)
    return ulst


# getting keys for unique values
def uniqueValues(aDict):
    kl = []
    p = lst(aDict)
    dict = ulistcount(p)
    ul = unique(dict)
    for e in ul:
        for k, v in aDict.items():
            if v == e:
                kl.append(k)
                kl.sort()
    return kl

print(uniqueValues({1: 1, 2: 2, 3: 3, 4:1})) #output [2, 3]
print(uniqueValues({0: 9, 1: 1, 2: 7, 3: 3, 5: 2, 6: 5, 7: 8, 9: 10, 10: 0})) # output [0, 1, 2, 3, 5, 6, 7, 9, 10]