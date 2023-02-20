def greedy_cow_transport(cows, limit=10):
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

    while len(cows) > 0:
        finalResult.append(start(cows))
    return finalResult
