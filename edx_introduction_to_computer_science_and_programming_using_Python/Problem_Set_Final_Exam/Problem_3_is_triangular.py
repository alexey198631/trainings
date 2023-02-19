"""
Write a function is_triangular that meets the specification below.
A triangular number is a number obtained by the continued summation of integers starting from 1.
For example, 1, 1+2, 1+2+3, 1+2+3+4, etc., corresponding to 1, 3, 6, 10, etc., are triangular numbers.

def is_triangular(k):
    k, a positive integer
    returns True if k is triangular and False if not
"""


def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not

    """
    sum = 0
    i = 1
    while sum < k:
        sum += i
        i += 1
    return sum == k


print(is_triangular(1)) # output: True
print(is_triangular(11)) # output: False
print(is_triangular(55)) # output: True