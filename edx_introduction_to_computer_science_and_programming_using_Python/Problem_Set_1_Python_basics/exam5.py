
aDict = {
    'b': 1,
    'a': 1,
    'c': 3,
    'd': 3
}

#creating list of all values from the dictionary - > list

def lst(aDict):
    val = []
    for v in aDict.values():
        val.append(v)
    return val

#counting values - > dict

def ulistcount(lst):
    counts = dict()
    for n in lst:
        counts[n] = counts.get(n,0) + 1
    return counts

#unique values - > list

def unique(ulistcount):
    ulst = []
    for k in ulistcount:
        if ulistcount[k] == 1:
            ulst.append(k)
    return ulst

#getting keys for unique values

def uniqueValues(aDict):
    kl = []
    p = lst(aDict)
    dict = ulistcount(p)
    ul = unique(dict)
    for e in ul:
        for k,v in aDict.items():
            if v == e:
                kl.append(k)
                kl.sort()
    return kl


print(uniqueValues(aDict))