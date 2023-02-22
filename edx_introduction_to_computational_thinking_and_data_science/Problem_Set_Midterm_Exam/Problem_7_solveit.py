"""
Write a function that meets the specification below:

def solveit(test):
    test, a function that takes an int parameter and returns a Boolean
    Assumes there exists an int, x, such that test(x) is True
    Returns an int, x, with the smallest absolute value such that test(x) is True
    In case of ties, return any one of them.

#### This test case prints 49 ####
def f(x):
    return (x+15)**0.5 + x**0.5 == 15
print(solveit(f))

#### This test case prints 0 ####
def f(x):
    return x == 0
print(solveit(f))
"""


def solveit(test):
    """ test, a function that takes an int parameter and returns a Boolean
        Assumes there exists an int, x, such that test(x) is True
        Returns an int, x, with the smallest absolute value such that test(x) is True
        In case of ties, return any one of them.
    """
    # IMPLEMENT THIS FUNCTION
    n = 0
    while True:
        # checks positive numbers
        if test(n):
            return n
        # checks negative numbers
        elif test(-n):
            return -n
        n += 1


# testing

def f(x):
    return (x + 15) ** 0.5 + x ** 0.5 == 15


print(solveit(f))  # output 49


def f(x):
    return x == 100


print(solveit(f))  # output 100


def f(x):
    return x ** 2 - 2 * x - 3 == 0


print(solveit(f))  # output -1
