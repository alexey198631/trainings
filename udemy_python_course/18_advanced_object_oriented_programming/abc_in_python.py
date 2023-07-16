"""
In Python, ABC stands for Abstract Base Class. An abstract base class is a class that cannot be instantiated and
is meant to serve as a blueprint for other classes. It provides a way to define a common interface and establish
a contract for subclasses to follow.

The main purpose of using ABCs in Python is to enforce a certain structure or behavior on the subclasses.
By defining methods in an abstract base class, you can ensure that the subclasses implement those methods,
making it easier to build a hierarchy of related classes with shared functionality.

Here are a few reasons why you might need to use ABCs in Python:

Defining a common interface: If you have a group of classes that need to share a common set of methods, you can define
those methods in an abstract base class. Subclasses are then required to implement those methods, ensuring consistency
across the hierarchy.

Polymorphism: ABCs enable polymorphic behavior, meaning you can treat different subclasses as interchangeable objects.
Since they adhere to the same interface defined in the abstract base class, you can write code that works with any
subclass without knowing the specific implementation details.

Documentation and clarity: By using ABCs, you can clearly communicate to other developers the expected structure and
behavior of subclasses. It serves as a form of documentation, making it easier for others (and even yourself) to
understand how to use and extend your code.

Error prevention: Abstract base classes can help prevent runtime errors by ensuring that subclasses implement necessary
methods. If a subclass fails to implement a required method, Python will raise an error when attempting to instantiate
the subclass.

"""
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rectangle = Rectangle(5, 3)
print(rectangle.area())      # Output: 15
print(rectangle.perimeter()) # Output: 16
