"""
Your task is to define the following two methods for the intSet class:

Define an intersect method that returns a new intSet containing elements that appear in both sets. In other words,

s1.intersect(s2)
would return a new intSet of integers that appear in both s1 and s2. Think carefully - what should happen if s1 and
s2 have no elements in common?

Add the appropriate method(s) so that len(s) returns the number of elements in s.
"""


class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def intersect(self, other):
        new = intSet()
        for e in self.vals:
            if other.member(e):
                new.insert(e)
        return new


    def __len__(self):
        return len(self.vals)

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ', '.join([str(e) for e in self.vals]) + '}'


s = intSet()
c = intSet()
setA = [-10, -5, 3, 4, 11, 15, 19, 20, 10]
setB = [-20, -16, -14, -6, -5, 0, 5, 10, 20]
for a in setA:
    s.insert(a)
for b in setB:
    c.insert(b)


print(s) # output {-10, -5, 3, 4, 10, 11, 15, 19, 20}
print(c) # output {-20, -16, -14, -6, -5, 0, 5, 10, 20}
print(s.intersect(c)) # output {-5, 10, 20}

