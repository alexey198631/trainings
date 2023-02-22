"""
In this problem, we will use the implementation you filled in for Problem 4 to run a simulation.
You will create a TreatedPatient instance with the following parameters, then run the simulation:

- viruses, a list of 100 ResistantVirus instances
- maxPop, maximum sustainable virus population = 1000

Each ResistantVirus instance in the viruses list should be initialized with the following parameters:

- maxBirthProb, maximum reproduction probability for a virus particle = 0.1
- clearProb, maximum clearance probability for a virus particle = 0.05
- resistances, The virus's genetic resistance to drugs in the experiment = {'guttagonol': False}
- mutProb, probability of a mutation in a virus particle's offspring = 0.005

Run a simulation that consists of 150 time steps, followed by the addition of the drug, guttagonol,
followed by another 150 time steps. You should make use of the function simulationWithDrug(numViruses,
maxPop, maxBirthProb, clearProb, resistances, mutProb, numTrials). As with problem 3, perform up to 100 trials and
make sure that your results are repeatable and representative.

Create one plot that records both the average total virus population and the average population of
guttagonol-resistant virus particles over time.

A few good questions to consider as you look at your plots are: What trends do you observe?
Are the trends consistent with your intuition? Feel free to discuss the answers to these questions in the forum,
to fully cement your understanding of this problem set, processing and interpreting data.
"""
import pylab
from Problem_4_TreatedPatient_Class import *


def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1).
    numTrials: number of simulation runs to execute (an integer)

    """

    data = [0] * 300
    data1 = [0] * 300

    for i in range(numTrials):
        virus = ResistantVirus(maxBirthProb, clearProb, resistances.copy(), mutProb)
        viruses = [virus] * numViruses
        patient = TreatedPatient(viruses, maxPop)
        virus_count = []
        resist_virus_count = []

        for j in range(300):
            if j == 150:
                patient.addPrescription('guttagonol')
            virus_count.append(patient.update())
            resist_virus_count.append(patient.getResistPop(['guttagonol']))

        for z in range(300):
            data[z] = data[z] + virus_count[z]

        for y in range(300):
            data1[y] = data1[y] + resist_virus_count[y]


    for m in range(300):
        data[m] = data[m] / numTrials

    for km in range(300):
        data1[km] = data1[km] / numTrials

    pylab.figure(figsize=(16, 10), dpi=80)

    pylab.get_current_fig_manager().set_window_title('Cool Name')

    pylab.plot(list(data), label=r'Non-resistant population')
    pylab.plot(list(data1), label=r'Guttagonol Resistant population')
    pylab.xlabel(r'Number of steps')
    pylab.ylabel(r'Average Virus Population')
    pylab.title(r'Virus Simulation in Patient')
    pylab.legend()
    pylab.show()


#simulationWithDrug(100, 1000, .1, 0.05, {"guttagonol": False}, 0.005, 100)
#simulationWithDrug(75, 100, .8, 0.1, {"guttagonol": True}, 0.8, 1)
simulationWithDrug(1, 20, 1.0, 0.0, {"guttagonol": True}, 1.0, 5)