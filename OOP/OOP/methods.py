class Cookie:
    chocolate = False

c = Cookie()
c.chocolate

c.chocolate = True
c.chocolate

# New method __init__
class Cookie():
    chocolate = False
    def __init__(self):
        print("A cookie was created")

c = Cookie()

# Example 1
class Cookie():
    chocolate = False
    def __init__(self):
        print("A cookie was created")
    def chocolater(self):
        self.chocolate = True
    def has_chocolate(self):
        if (self.chocolate):
            print("The cookie has chocolate")
        else:
            print("The cookie has NOT chocolate")

c = Cookie()
c.has_chocolate()
c.chocolater()
c.has_chocolate()

# Example 2
class Cookie():
    chocolate = False
    def __init__(self, color = None, flavor = None):
        self.color = color
        self.flavor = flavor
        if color is not None and flavor is not None:
            print("A {} {} cookie was created".format(color, flavor))
    def chocolater(self):
        self.chocolate = True
    def has_chocolate(self):
        if (self.chocolate):
            print("The cookie has chocolate")
        else:
            print("The cookie has NOT chocolate")

c = Cookie("orange", "sugar")
g = Cookie()
