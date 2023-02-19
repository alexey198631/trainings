"""
Write a Python function that takes in two lists and calculates whether they are permutations of each other.
The lists can contain both integers and strings. We define a permutation as follows:

- the lists have the same number of elements
- list elements appear the same number of times in both lists
- If the lists are not permutations of each other, the function returns False.

If they are permutations of each other, the function returns a tuple consisting of the following elements:

- the element occuring the most times
- how many times that element occurs
- the type of the element that occurs the most times

If both lists are empty return the tuple (None, None, None).
If more than one element occurs the most number of times, you can return any of them.

For example,

if L1 = ['a', 'a', 'b'] and L2 = ['a', 'b'] then is_list_permutation returns False
if L1 = [1, 'b', 1, 'c', 'c', 1] and L2 = ['c', 1, 'b', 1, 1, 'c'] then is_list_permutation returns
(1, 3, <class 'int'>) because the integer 1 occurs the most, 3 times, and the type of 1 is an integer
(note that the third element in the tuple is not a string).
"""


def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other.
            If they are permutations of each other, returns a
            tuple of 3 items in this order:
            the element occurring most, how many times it occurs, and its type
    '''
    # determine key from value in a dictionary
    def get_key(dct, value):
        for k, v in dct.items():
            if v == value:
                return k

    len1 = len(L1)
    len2 = len(L2)
    # the lists have the same number of elements, otherwise - False
    if len1 != len2:
        return False
    # if both lists are empty return the tuple (None, None, None)
    elif len1 == 0:
        return None, None, None
    # if both lists have just one element
    elif len1 == 1:
        return L1[0], 1, type(L1[0])
    else:
        # dictionary with count of unique elements in both lists
        elements1 = dict((x, L1.count(x)) for x in set(L1) if L1.count(x) >= 1)
        elements2 = dict((x, L2.count(x)) for x in set(L2) if L2.count(x) >= 1)
        # elements1 and elements2 have the same key-value pairs, so they are equal
        if elements1 == elements2:
            # how many times the element occuring the most times occurs
            maxim = max(elements1.values())
            # the element occuring the most times
            key = get_key(elements1, maxim)
            # the type of the element that occurs the most times
            tp = type(key)
            return key, maxim, tp
        else:
            return False


L1 = ['a', 'a', 'b']
L2 = ['a', 'b']

print(is_list_permutation(L1, L2)) # output: False

L1 = [1, 'b', 1, 'c', 'c', 1]
L2 = ['c', 1, 'b', 1, 1, 'c']

print(is_list_permutation(L1, L2)) # output: (1, 3, <class 'int'>)