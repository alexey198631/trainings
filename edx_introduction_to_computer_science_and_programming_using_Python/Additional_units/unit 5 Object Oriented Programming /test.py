class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self, time):
        print(time)

clock = Clock('5:30')
print(clock)
clock.print_time('10:30')

X = 7
Y = 8

class Weird(object):
    def __init__(self, x, y):
        self.y = y
        self.x = x
    def getX(self):
        return x
    def getY(self):
        return y

class Wild(object):
    def __init__(self, x, y):
        self.y = y
        self.x = x
    def getX(self):
        return self.x
    def getY(self):
        return self.y




#w1 = Weird(X, Y)
#print(w1.getX())





r = 'aaysogs'
p = 'as'

list = []

for j in range(len(p)):
    for i in range(len(r)):

        if r[i] != p[j]:
            list.append(r[i])


print(list)
