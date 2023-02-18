"""
Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method:
2, 3, 5, 7, 11, ...
"""
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
for i in range(0, 100):
    print(n.__next__()) # output 2, 3, 5, 7, 11, ..., 541