def program1(x):
    step = 0
    total = 0
    step += 1

    for i in range(1000):
        step += 1
        total += i
        step += 1

    while x > 0:
        step += 1
        x -= 1
        step += 1
        total += x
        step += 1

    step += 1

    return total, step + 1

def program2(x):
    step = 0
    total = 0
    step += 1
    for i in range(1000):
        step += 1
        total = i
        step += 1

    while x > 0:
        step += 1
        x = x//2
        step += 1
        total += x
        step += 1

    step += 1


    return total, step + 1

def program3(L):
    step = 0
    totalSum = 0
    step += 1
    highestFound = None
    step += 1
    for x in L:
        step += 1
        totalSum += x
        step += 1

    for x in L:
        step += 1
        if highestFound == None:
            step += 1
            highestFound = x
            step += 1
        elif x > highestFound:
            step += 1
            highestFound = x
            step += 1

    return (totalSum, highestFound, step + 1)

print(program1(1))




print(program2(5))

print(program3([1]))


def program11(L):
    step = 0
    multiples = []
    step += 1
    for x in L:
        step += 1
        print('1', step)
        for y in L:
            step += 1
            multiples.append(x*y)
            step += 1
            step += 1
            print('2', step)
    return multiples, step + 1

#print(program11([1,2,3,4]))

#  (3 * n + 1) * n + 2 = 3 * n ^ 2 + n + 2

def program22(L):
    step = 0
    squares = []
    step += 1
    for x in L:
        step += 1
        print('1', step)
        for y in L:
            step += 1
            print('2', step)
            if x == y:
                step += 1
                squares.append(x*y)
                step += 1
                step += 1
                print('3', step)
    return squares, step + 1

#print(program22([2,2,2,2]))

# n * (4n + 1) + 2 = 4 * n ^ 2 + n + 2

def program33(L1, L2):
    step = 0
    intersection = []
    step += 1
    for elt in L1:
        step += 1
        if elt in L2:
            step += 1 * len(L2)
            intersection.append(elt)
            step += 1
    return intersection, step + 1

print(program33([3,3,3],[1,2,3]))

# n^2 + 2*n + 2        1 + (n + 2)* n + 1


# n ^ 2 + 2 n