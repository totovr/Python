class Vehicle():

    def __init__(self, color, wheels):
        self.color = color
        self.wheels = wheels

    def __str__(self):
        return "color {}, {} wheels".format( self.color, self.wheels )


class Car(Vehicle):

    def __init__(self, color, wheels, speed, cc):
        self.color = color
        self.wheels = wheels
        self.speed = speed
        self.cc = cc

    def __str__(self):
        return "color {}, {} km/h, {} wheels, {} cc".format( self.color, self.speed, self.wheels, self.cc )


c = Car("blue", 150, 4, 1200)
print(c)


# The most obvious drawback of overwriting is that we have to rewrite the code of the superclass and then
# the specific subclass code.

class Vehicle():

    def __init__(self, color, wheels):
        self.color = color
        self.wheels = wheels

    def __str__(self):
        return "color {}, {} wheels".format( self.color, self.wheels )


class Car(Vehicle):

    def __init__(self, color, wheels, speed, cc):
        Vehicle.__init__(self, color, wheels)
        self.speed = speed
        self.cc = cc

    def __str__(self):
        return Vehicle.__str__(self)+ ", {} wheels, {} cc".format( self.color, self.speed, self.wheels, self.cc )


c = Car("blue", 150, 4, 1200)
print(c)


# We can use the method super() in this way it also allows us to comfortably
# call the methods or attributes of the superclass without the need to specify
# the self.

class Vehicle():

    def __init__(self, color, wheels):
        self.color = color
        self.wheels = wheels

    def __str__(self):
        return "color {}, {} wheels".format( self.color, self.wheels )


class Car(Vehicle):

    def __init__(self, color, wheels speed, cc):
        super().__init__(color, wheels) # We use super() instead of Vehicle and without self
        self.speed = speed
        self.cc = cc

    def __str__(self):
        return super().__str__()+ ", {} wheels, {} cc".format( self.wheels, self.cc )


c = Car("blue", 4, 150, 1200)
print(c)
