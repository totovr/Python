import math

class Point:

    def __init__(self, x = 0, y = 0 ):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def quadrant(self):
        if (self.x > 0 and self.y > 0):
            print("{} belongs to first quadrant".format(self))
        elif (self.x < 0 and self.y > 0):
            print("{} belongs to second quadrant".format(self))
        elif (self.x < 0 and self.y < 0):
            print("{} belongs to third quadrant".format(self))
        elif (self.x > 0 and self.y < 0):
            print("{} belongs to fourth quadrant".format(self))
        else:
            print("{} is located in the origin".format(self))

    def vector(self, p):
        print("The vector bettwen {} and {} is ({}, {})".format(self, p, p.x - self.x, p.y - self.y))

    def distance(self, p):
        d = math.sqrt( (p.x - self.x)**2 + (p.y - self.y)**2 )
        print("The distance between the points {} and {} is {}".format(self, p, d))

A = Point(2,3)
B = Point(5,5)
C = Point(-3,-1)
D = Point(0,0)

# A.quadrant()
# B.quadrant()
# C.quadrant()
# D.quadrant()

# Here is as if we assign p = B
# A.vector(B)
# B.vector(A)

A.distance(D)
B.distance(D)
C.distance(D)

# Second example

class Rectangle:

    def __init__(self, pInitial = Point(), pFinal = Point()):
        self.pInitial = pInitial
        self.pFinal = pFinal

    def base(self):
        self.base = abs(self.pFinal.x - self.pInitial.x)
        print("The base of the rectangle is {}".format(self.base))

    def altitud(self):
        self.alt = abs(self.pFinal.y - self.pInitial.y)
        print("The altitud of the rectangle is {}".format(self.alt))

    def area(self):
        self.a = self.base * self.alt
        print("The area of the rectangle is {}".format(self.a))

R = Rectangle(A,B)
R.base()
R.altitud()
R.area()
