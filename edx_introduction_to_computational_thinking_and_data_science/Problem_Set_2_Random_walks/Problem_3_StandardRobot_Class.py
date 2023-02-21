"""
Each robot must also have some code that tells it how to move about a room,
which will go in a method called updatePositionAndClean.

Ordinarily we would consider putting all the robot's methods in a single class.
However, later in this problem set we'll consider robots with alternate movement strategies, to be implemented
as different classes with the same interface. These classes will have a different implementation of
updatePositionAndClean but are for the most part the same as the original robots.
Therefore, we'd like to use inheritance to reduce the amount of duplicated code.

We have already refactored the robot code for you into two classes:
the Robot class you completed in Problem 2 (which contains general robot code),
and a StandardRobot class that inherits from it (which contains its own movement strategy).
"""
import random
from Problem_1_RectangularRoom_Class import Position, RectangularRoom


class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """

    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.speed = speed
        self.robotDirection = random.uniform(0, 360)
        self.robotPosition = self.room.getRandomPosition()
        self.room.cleanTileAtPosition(self.robotPosition)

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.robotPosition

    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.robotDirection

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.robotPosition = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.robotDirection = direction

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError  # don't change this!


# === Problem 3
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """

    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        self.newPosition = Position.getNewPosition(self.getRobotPosition(), self.robotDirection, self.speed)
        if self.room.isPositionInRoom(self.newPosition):
            self.setRobotPosition(self.newPosition)
            self.room.cleanTileAtPosition(self.getRobotPosition())
        else:
            self.setRobotDirection(random.uniform(0, 360))


"""
# some code testing
random.seed(0)
robot = Robot(RectangularRoom(1,2), 1.0)
print(robot.getRobotPosition()) # output: (0.76, 0.84)

robot = Robot(RectangularRoom(5, 8), 1.0)
robot.getRobotDirection()
for i in range(10):
    randDirection = random.randint(0, 361)
    robot.setRobotDirection(randDirection)
    print('Random direction:', robot.getRobotDirection())"""