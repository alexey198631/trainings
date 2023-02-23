"""
For this problem you are going to simulate growth of fox and rabbit population in a forest!

The following facts are true about the fox and rabbit population:

The maximum population of rabbits is determined by the amount of vegetation in the forest, which is relatively stable.
There are never fewer than 10 rabbits; the maximum population of rabbits is 1000.
For each rabbit during each time step, a new rabbit will be born with a probability of

In other words, when the current population is near the maximum, the probability of giving birth is very low,
and when the current population is small, the probability of giving birth is very high.

The population of foxes is constrained by number of rabbits.

There are never fewer than 10 foxes.
At each time step, after the rabbits have finished reproducing, a fox will try to hunt a rabbit with success rate of
In other words, the more rabbits, the more likely a fox will eat one.

If a fox succeeds in hunting, it will decrease the number of rabbits by 1 immediately. Remember that the population of
rabbits is never lower than 10.

Additionally, if a fox succeeds in hunting, then it has a 1/3 probability of giving birth in the current time-step.

If a fox fails in hunting then it has a 10 percent chance of dying in the current time-step.
If the starting population is below 10 then you should do nothing. You should not increase the population nor set the
population to 10.
Start with 500 rabbits and 30 foxes.

At the end of each time step, record the number of foxes and rabbits.

Run the simulation for 200 time steps, and then plot the population of rabbits and the population of foxes as a
function of time step. (You do not need to paste your code for plotting for Part A of this problem).

Step 1: Write the procedure, rabbitGrowth, that updates the number of rabbits during the first part of a time step
Step 2: Write the procedure, foxGrowth, that updates the number of rabbits and foxes during the second part of a time
step
Step 3: Write the master procedure, runSimulation, that loops for some amount of time steps, doing the first part and
then the second part of the simulation. Record the two populations in two different lists, and return those lists.
"""
import random
import pylab



# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30


def rabbitGrowth():
    """
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up,
      a new rabbit may be born.
    Nothing is returned.
    """
    # you need this line for modifying global variables
    global CURRENTRABBITPOP

    for i in range(CURRENTRABBITPOP):
        if random.random() <= (1 - CURRENTRABBITPOP / MAXRABBITPOP):
            CURRENTRABBITPOP += 1

def foxGrowth():
    """
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    # you need these lines for modifying global variables
    global CURRENTRABBITPOP
    global CURRENTFOXPOP

    # TO DO
    for i in range(CURRENTFOXPOP):
        if CURRENTRABBITPOP > 10:
            if random.random() <= (CURRENTRABBITPOP / MAXRABBITPOP):
                CURRENTRABBITPOP -= 1
                if random.random() <= (1 / 3):
                    CURRENTFOXPOP += 1
            else:
                if random.random() <= 0.9:
                    CURRENTFOXPOP -= 1


def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """

    rabbits = []
    foxes = []

    for i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbits.append(CURRENTRABBITPOP)
        foxes.append(CURRENTFOXPOP)
    return rabbits, foxes


pylab.plot(runSimulation(numSteps = 100)[0], color='grey', label='Rabbits')
pylab.plot(runSimulation(numSteps = 100)[1], color='red', label='Foxes')
pylab.legend(loc='upper right')
pylab.xlabel('Time Steps')
pylab.ylabel('Population')
pylab.show()



MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30
numSteps = 200

rab_pop, fox_pop = runSimulation(numSteps=numSteps)

pylab.plot(rab_pop, color='grey', label='Rabbits')
pylab.plot(fox_pop, color='red', label='Foxes')
pylab.legend(loc='upper right')
pylab.xlabel('Time Steps')
pylab.ylabel('Population')
pylab.figure('Fox / Rabit Populations')

"""
Use polyfit to find the coefficients of a 2nd degree polynomial for the rabbit curve and the same for the fox curve. 
Then use polyval to evaluation the 2nd degree polynomial and plot it, e.g.

coeff = polyfit(range(len(rabbitPopulationOverTime)), rabbitPopulationOverTime, 2)
plot(polyval(coeff, range(len(rabbitPopulationOverTime))))

Of course your variables and plotting commands may not look identical to the above code; 
the above code is shown just to give you an idea of what we mean.
"""


pylab.figure('Fox / Rabit Populations')
degree = 2
rab_coeff = pylab.polyfit(range(len(rab_pop)), rab_pop, degree)
pylab.plot(pylab.polyval(rab_coeff, range(len(rab_pop))), 'b-')
fox_coeff = pylab.polyfit(range(len(fox_pop)), fox_pop, degree)
pylab.plot(pylab.polyval(fox_coeff, range(len(fox_pop))), 'r-')
pylab.xlabel('Time Steps')
pylab.ylabel('Population')
pylab.legend(loc='upper right')
pylab.show()