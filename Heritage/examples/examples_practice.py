class Vehicle():

    def __init__(self, color, wheels):
        self.color = color
        self.wheels = wheels

    def __str__(self):
        return "Color {}, {} wheels".format( self.color, self.wheels )


class Car(Vehicle):

    def __init__(self, color, wheels, speed, cc):
        super().__init__(color, wheels)
        self.speed = speed
        self.cc = cc

    def __str__(self):
        return super().__str__()+ ", {} Km/h, {} cc".format( self.speed, self.cc )

class Truck(Car):

    def __init__(self, color, wheels, speed, cc, load):
        super().__init__(color, wheels, speed, cc)
        self.load = load

    def __str__(self):
        return super().__str__()+ ", {} tons / load".format( self.load )

class Bicycle(Vehicle):

    def __init__(self, color, wheels, type):
        super().__init__(color, wheels)
        self.type = type

    def __str__(self):
        return super().__str__()+ ", {} type".format( self.type )

class Motorbike(Bicycle):
    def __init__(self, color, wheels, type, speed, cc):
        super().__init__(color, wheels, type)
        self.speed = speed
        self.cc = cc

    def __str__(self):
        return super().__str__()+ ", {} Km/h, {} cc".format( self.speed, self.cc )


vehicles = [
    Car("black", 4, 190, 2000),
    Truck("white", 4, 180, 3500, 10000),
    Bicycle("red", 2, "sport"),
    Motorbike("blue", 2, "sport", 320, 1000)
    ]


# def catalogue(list_vehicles):
#     for v in list_vehicles:
#         print("{} {}".format(type(v).__name__, v))
#
# catalogue(vehicles)

def catalogue(list_vehicles, wheels = None):

    c = 0
    if wheels != None:
        for v in list_vehicles:
            if v.wheels == wheels:
                c += 1
        print("We found {} vehicles with {} wheels".format( c, wheels ))

    for v in list_vehicles:
        if wheels == None:
            print("{} {}".format(type(v).__name__, v))
        else:
            if v.wheels == wheels:
                print("{} {}".format(type(v).__name__, v))

catalogue(vehicles, 2)
