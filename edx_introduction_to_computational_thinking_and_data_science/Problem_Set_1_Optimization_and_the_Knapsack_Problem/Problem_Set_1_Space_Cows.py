###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    class Cow(object):
        def __init__(self, n, w):
            self.name = n
            self.weight = w

        def getWeight(self):
            return self.weight

        def __str__(self):
            return self.name

    def loadShip(names, weights):
        ShipList = []
        for i in range(len(weights)):
            ShipList.append(Cow(names[i], weights[i]))
        return ShipList

    def greedz(cow, maxWeight, keyFunction):
        """Assumes cow a list, maxWeight >= 0,
             keyFunction maps elements of items to numbers"""
        cowCopy = sorted(cow, key=keyFunction,
                         reverse=True)
        result = []
        totalWeight = 0.0
        for i in range(len(cowCopy)):
            if (totalWeight + cowCopy[i].getWeight()) <= maxWeight:
                result.append(cowCopy[i])
                totalWeight += cowCopy[i].getWeight()
        return result

    finalResult = []

    def start(dct):
        names = []
        weights = []
        intResult = []
        for k, v in dct.items():
            names.append(k)
            weights.append(v)
        cows = loadShip(names, weights)
        for t in greedz(cows, limit, Cow.getWeight):
            intResult.append(str(t))
            dct.pop(str(t))
        return intResult

    copydct = cows.copy()

    while len(copydct) > 0:
        finalResult.append(start(copydct))

    return finalResult


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    class Cow(object):
        def __init__(self, n, w):
            self.name = n
            self.weight = w

        def getName(self):
            return self.name

        def getWeight(self):
            return self.weight

        def __str__(self):
            return self.name


    def get_key(d, value):
        for k, v in d.items():
            if v == value:
                return k

    def listsum(numList):
        if len(numList) == 1:
            return numList[0]
        else:
            return numList[0] + listsum(numList[1:])

    names = []
    weights = []
    for k, v in cows.items():
        names.append(k)
        weights.append(v)

    min = len(weights)
    for item in (get_partitions(weights)):
        count = 0
        for i in item:
            if listsum(i) <= limit:
                count += 1
        if len(item) == count:
            if min > len(item):
                min = len(item)
            if len(item) == min:
                new = []
                for p in item:
                    inter = []
                    for n in range(len(p)):
                        inter.append(get_key(cows, p[n]))
                    new.append(inter)
                break
    return new


# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=10
print(cows)

print(greedy_cow_transport(cows, limit))
print(brute_force_cow_transport(cows, limit))


