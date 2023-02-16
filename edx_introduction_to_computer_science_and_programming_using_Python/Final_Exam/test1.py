def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not

    Write a function is_triangular that meets the specification below. A triangular number is a number obtained by the continued summation of integers starting from 1. For example, 1, 1+2, 1+2+3, 1+2+3+4, etc., corresponding to 1, 3, 6, 10, etc., are triangular numbers.
    """
    result = False
    doublek = k * 2
    lst = []
    for i in range(1,k):
        lst.append(i)
    for p in lst:
        print(p*(p+1))
        if p*(p+1) == doublek:
            result = True
            return result
            break
        else:
            continue
    if k == 1:
        result = True
        return result
    return result

print(is_triangular(6))






