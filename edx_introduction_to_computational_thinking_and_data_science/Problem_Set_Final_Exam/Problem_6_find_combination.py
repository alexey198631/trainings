"""
Write a function that meets the specifications below. You do not have to use dynamic programming.

Hint: You might want to use bin() on an int to get a string, get rid of the first two characters,
add leading 0's as needed, and then convert it to a numpy array of ints. Type help(bin) in the console.

For example,

If choices = [1,2,2,3] and total = 4 you should return either [0 1 1 0] or [1 0 0 1]
If choices = [1,1,3,5,3] and total = 5 you should return [0 0 0 1 0]
If choices = [1,1,1,9] and total = 4 you should return [1 1 1 0]

"""


import numpy as np

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int

    Returns result, a numpy.array of length len(choices)
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total,
    pick the one that gives sum(result*choices) closest
    to total without going over.
    """

    def str_to_int(lst):
        for i in range(len(lst)):
            lst[i] = int(lst[i])
        return lst

    def zeros(total):
        result = []
        z = '0'
        t = '1'
        num = int(t * total, 2)
        for c in range(num + 1):
            x = str(bin(c))[2:]
            if len(x) != total:
                x = z * (total - len(x)) + x
            result.append(list((x)))

        for lst in result:
            str_to_int(lst)

        return result


    result_ok = []
    result_less = []
    comb = zeros(len(choices))
    step1 = np.array(choices)
    result = np.array(comb[0])

    for l in comb:
        arr_l = np.array(l)
        sum_to_check = sum(arr_l * step1)
        if sum_to_check == total:
            result_ok.append(arr_l)
        elif sum_to_check < total:
            result_less.append(arr_l)

    if len(result_ok) > 0:
        minim = sum(choices)
        for ar in result_ok:
            if sum(ar) < minim:
                minim = sum(ar)
                result = ar
        return result

    else:
        maxim = 0
        for ar in result_less:
            if sum(ar) > maxim:
                maxim = sum(ar)
                result = ar
        return result


# testing
print(find_combination([1, 2, 2, 3], 4)) # output: [0 1 1 0 0]
print(find_combination([1, 1, 3, 5, 3], 5)) # output: [0 0 0 1 0]
print(find_combination([1, 1, 1, 9], 4)) # output: [1 1 1 0]
print(find_combination([3, 10, 2, 1, 5], 12)) # output: [0 1 1 0 0]