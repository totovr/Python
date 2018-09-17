def greetings():
    print("Hello, this is the greeting function")

greetings()

def table_five():
    for i in range(10):
        print("5 *", i, "=", i * 5)
table_five()

# local variables
def test():
    n = 10
test()
# This will throw an error
n

# global variables
n = 10
def test():
    n = 10
test()
# This will not throw an error
n

# Varibles with the same name can coexist but is not recomendable
def test():
    n = 10
    print(n)
n = 5
test()
print(n)
