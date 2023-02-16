def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other.
            If they are permutations of each other, returns a
            tuple of 3 items in this order:
            the element occurring most, how many times it occurs, and its type
    '''
    def get_key(dict, value):
        for k, v in dict.items():
            if v == value:
                return k

    len1 = len(L1)
    len2 = len(L2)
    if len1 != len2:
        return False
    elif len1 == 0:
        return None, None, None
    elif len1 == 1:
        return L1[0], 1, type(L1[0])
    else:
        elements1 = dict((x, L1.count(x)) for x in set(L1) if L1.count(x) >= 1)
        elements2 = dict((x, L2.count(x)) for x in set(L2) if L2.count(x) >= 1)
        if elements1 == elements2:
            maxim = max(elements1.values())
            key = get_key(elements1, maxim)
            tp = type(key)
            return key, maxim, tp
        else:
            return False



L1 = [1, 'b', 1, 'c', 'c', 1]
L2 = ['c', 1, 'b', 1, 1, 'c']


print(is_list_permutation(L1, L2))