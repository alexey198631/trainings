def brute_force_cow_transport(cows, limit=10):
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

    def app(lst, limit):
        check = [number <= limit for number in lst]
        res = all(x == True for x in check)
        return res

    copy_cows = cows.copy()
    names = []
    weights = []
    for k, v in copy_cows.items():
        names.append(k)
        weights.append(v)

    mn = len(weights)

    cnt = []

    for item in (get_partitions(names)):

        new = []
        count = 0
        for p in item:
            inter = []
            for n in range(len(p)):
                inter.append(copy_cows[p[n]])

            new.append(listsum(inter))
            count += 1

        if app(new, limit):
            # print(new, count, mn)
            if len(item) == count:
                # print('min', mn)
                if len(item) <= mn:
                    mn = len(item)
                    # print('here', item)
                    cnt.append(item)
                    # print('len', len(cnt))

    if len(cnt) == 1:
        return cnt[0]
    else:
        x = (len(cnt)) - 1
        return cnt[x]