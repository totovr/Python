class Movie:
    # This is the constructor
    def __init__(self, title, time, launched):
        self.title = title
        self.time = time
        self.launched = launched
        print("The movie {} was created".format(self.title))

    # Destructor
    def __del__(self):
        print("The movie {} was delated ".format(self.title))

    # Redefine string
    def __str__(self):
        return "{} was relased in {} and has a duration of {}".format(self.title, self.launched, self.time)

    # Redefine the method lenght
    def __len__(self):
        return self.time

m = Movie("the Good father", 175, 1972)

# To erase the constructor
# del(m)

m

str(m)

len(m)
