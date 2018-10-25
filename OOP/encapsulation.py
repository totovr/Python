# Functionality to make it private the elements of the methods
class Example:
    __private_attribute = "This attribute can not be reach from outside"

    def __private_method():
        print("This method can not be reached")

e = Example()
e.__private_attribute
e.__private_method()

# This is the way to make it public
class Example:
    __private_attribute = "This attribute can not be reach from outside"

    def __private_method(self):
        print("This method can not be reached from outside")

    def make_public_attribute(self):
        return self.__private_attribute

    def make_public_method(self):
        return self.__private_method()

e = Example()
e.make_public_attribute()
e.make_public_method()
