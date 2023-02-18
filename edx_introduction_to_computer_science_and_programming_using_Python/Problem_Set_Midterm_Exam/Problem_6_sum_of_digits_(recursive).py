"""
Write a recursive Python function, given a non-negative integer N, to calculate and return the sum of its digits.

Hint: Mod (%) by 10 gives you the rightmost digit (126 % 10 is 6), while doing integer division by 10 removes
the rightmost digit (126 // 10 is 12).

This function has to be recursive; you may not use loops!
This function takes in one integer and returns one integer.
"""


def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    if N == 0:
        return 0
    else:
        sum = N % 10

    return sum + sumDigits(N//10)


# testing of sumDigits()
# creation a list of random numbers
import random
random_numbers = []
for i in range(5):
    random_numbers.append(random.randint(1, 100))
# printing of the test results
for example in random_numbers:
    print(f'Sum of digits in {example} = {sumDigits(example)}')
