import numpy as np


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
    result_ok = []
    result_less = []
    comb = zeros(total)
    step1 = np.array(choices)

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


print(find_combination([1,3,0,0], 4))