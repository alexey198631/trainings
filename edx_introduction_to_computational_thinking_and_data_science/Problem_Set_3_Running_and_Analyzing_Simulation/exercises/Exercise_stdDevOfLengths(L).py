"""
Write a function, stdDevOfLengths(L) that takes in a list of strings, L, and outputs the standard deviation of the
lengths of the strings. Return float('NaN') if L is empty.
"""


def getMeanAndStd(X):
    mean = sum(X) / float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean) ** 2
    std = (tot / len(X)) ** 0.5
    return mean, std


def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) == 0:
        return float('NaN')
    else:
        list_of_len = []

        for l in L:
            list_of_len.append(len(l))

    return getMeanAndStd(list_of_len)[1]


# test cases

L = ['a', 'z', 'p']
print(stdDevOfLengths(L))  # output 0

L = ['apples', 'oranges', 'kiwis', 'pineapples']
print(stdDevOfLengths(L))  # output: 1.8708.