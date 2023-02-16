def primes():
    x = 1
    while True:
        count = 0
        x += 1
        for i in range(2, x):
            if x % i == 0:
                count += 1
        if count == 0:
            yield x


n = primes()
print(n.__next__())
print(n.__next__())
print(n.__next__())
print(n.__next__())
print(n.__next__())
print(n.__next__())
print(n.__next__())
print(n.__next__())


"""


# Note that our solution makes use of the for/else clause, which 
# you can read more about here:
# http://docs.python.org/release/1.5/tut/node23.html 

def genPrimes():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last

"""
