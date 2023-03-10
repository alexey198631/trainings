"""
Implementation of methods for the Robot class:

- Initializing the object
- Accessing the robot's position
- Accessing the robot's direction
- Setting the robot's position
- Setting the robot's direction

Note: When a Robot is initialized, it should clean the first tile it is initialized on.
Generally the model these Robots will follow is that after a robot lands on a given tile,
we will mark the entire tile as clean. This might not make sense if you're thinking about really large tiles,
but as we make the size of the tiles smaller and smaller, this does actually become a pretty good approximation.
"""
import math
import random
from Problem_1_RectangularRoom_Class import Position


class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """

    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        self.CleanedTiles = {}

    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        self.CleanedTiles[math.floor(pos.getX()), math.floor(pos.getY())] = 1

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        if (m, n) in self.CleanedTiles:
            return True
        else:
            return False

    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return int(self.width * self.height)

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        return int(len(self.CleanedTiles))

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        posX = random.uniform(0, self.width)
        posY = random.uniform(0, self.height)
        return Position(posX, posY)

    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        if 0 <= pos.getX() < self.width and 0 <= pos.getY() < self.height:
            return True
        else:
            return False


# === Problem 2
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