# If we just want to import one function we can write
# from greetings import greeting
# greeting()

# if we want to import all the functions we have to write
#from greetings import *
#greeting()

# Import a module that is located in a different path
# To import the module that we create in the sys path
import sys

sys.path.insert(1, '..')
# print(sys.path)

# With this we will import just the class
from greetings import Greeting

Greeting()
