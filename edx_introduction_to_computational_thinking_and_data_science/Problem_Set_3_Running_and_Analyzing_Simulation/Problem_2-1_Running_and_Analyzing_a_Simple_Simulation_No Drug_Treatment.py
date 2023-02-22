"""
You should start by understanding the population dynamics before introducing any drug.

Fill in the function simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb, numTrials)
that instantiates a Patient, simulates changes to the virus population for 300 time steps
(i.e., 300 calls to update), and plots the average size of the virus population as a function of time; that is,
the x-axis should correspond to the number of elapsed time steps, and the y-axis should correspond to the average
size of the virus population in the patient. The population at time=0 is the population after the first call to update.

Run the simulation for numTrials trials, where numTrials in this case can be up to 100 trials. Use pylab to produce
a plot (with a single curve) that displays the average result of running the simulation for many trials.
Make sure you run enough trials so that the resulting plot does not change much in terms of shape and time steps
taken for the average size of the virus population to become stable. Don't forget to include axes labels,
a legend for the curve, and a title on your plot.

You should call simulationWithoutDrug with the following parameters:

- numViruses = 100
- maxPop (maximum sustainable virus population) = 1000
- maxBirthProb (maximum reproduction probability for a virus particle) = 0.1
- clearProb (maximum clearance probability for a virus particle) = 0.05

Thus, your simulation should be instantiatating one Patient with a list of 100 SimpleVirus instances.
Each SimpleVirus instance in the viruses list should be initialized with the proper values for maxBirthProb
and clearProb.
"""


import pylab
from Problem_1_Implementing_a_Simple_Simulation_No_Drug_Treatment import Patient, SimpleVirus


def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    data = [0] * 300
    for k in range(numTrials):

        virus = SimpleVirus(maxBirthProb, clearProb)
        viruses = [virus] * numViruses

        vc = []
        patient = Patient(viruses, maxPop)

        for n in range(300):
            patient.update()
            vc.append(patient.getTotalPop())

        for o in range(300):
            data[o] = data[o] + vc[o]

    for m in range(300):
        data[m] = data[m] / numTrials

    pylab.plot(list(data), label=r'Average SimpleVirus Population')
    pylab.xlabel(r'Number of steps')
    pylab.ylabel(r'Virus Population')
    pylab.title(r'Simple Virus Simulation in Patient')
    pylab.legend()
    pylab.show()


# testing

simulationWithoutDrug(100, 1000, 0.1, 0.05, 100)