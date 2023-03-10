"""
Implement the following function:

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):

    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

The first six parameters should be self-explanatory. For the time being, you should pass in StandardRobot
for the robot_type parameter, like so:

avg = runSimulation(10, 1.0, 15, 20, 0.8, 30, StandardRobot)
Then, in runSimulation you should use robot_type(...) instead of StandardRobot(...) whenever you wish to instantiate
a robot. (This will allow us to easily adapt the simulation to run with different robot implementations,
which you'll encounter in Problem 6.)

For your reference, here are some approximate room cleaning times. These times are with a robot speed of 1.0.

One robot takes around 150 clock ticks to completely clean a 5x5 room.
One robot takes around 190 clock ticks to clean 75% of a 10x10 room.
One robot takes around 310 clock ticks to clean 90% of a 10x10 room.
One robot takes around 3322 clock ticks to completely clean a 20x20 room.
Three robots take around 1105 clock ticks to completely clean a 20x20 room.

(These are only intended as guidelines. Depending on the exact details of your implementation,
you may get times slightly different from ours.)
"""
from Problem_1_RectangularRoom_Class import RectangularRoom
from Problem_3_StandardRobot_Class import StandardRobot

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """

    trials = []

    # Run num_trials amount of tests
    for trial in range(num_trials):
        room = RectangularRoom(width, height)
        robotList = []
        for n in range(num_robots):
            robotList.append(robot_type(room, speed))
    steps = 0
    while (1.0 * room.getNumCleanedTiles() / room.getNumTiles()) <= min_coverage:
        for robot in robotList:
            robot.updatePositionAndClean()
        steps += 1
    trials.append(steps)
    return float(sum(trials)) / len(trials)


#avg = runSimulation(10, 1.0, 10, 12, 0.96, 30, StandardRobot)
#print(avg)