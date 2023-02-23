"""
Problem 4-1
Write a function called makeHistogram(values, numBins, xLabel, yLabel, title=None), with the  specification.

Problem 4-2
Write a function called getAverage(die, numRolls, numTrials)

A run of numbers counts the number of times the same dice value shows up in consecutive rolls. For example:

a dice roll of 1 4 3 has a longest run of 1
a dice roll of 1 3 3 2 has a longest run of 2
a dice roll of 5 4 4 4 5 5 2 5 has a longest run of 3

When this function is called with the test case given in the file, it will return 5.312. Your simulation may give
slightly different values.

"""
import pylab


# helper code
import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std


# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)


# problem 4-1
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    pylab.hist(values, bins=numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title != None:
        pylab.title(title)

    pylab.show()


#problem 4-2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    longest_runs = []
    for n in range(numTrials):
        rw = [die.roll() for j in range(numRolls)]
        size = 1
        max_size = 0
        for e in range(len(rw) - 1):
            if rw[e + 1] == rw[e]:
                size += 1
            else:
                size = 1
            if max_size < size:
                max_size = size
        if max_size > 0:
            longest_runs.append(max_size)
        else:
            longest_runs.append(1)

    mn = sum(longest_runs) / len(longest_runs)
    makeHistogram(longest_runs, 10, 'Length of the longest run', 'frequency', 'The longest runs')

    return round(mn, 3)


# One test case
print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))