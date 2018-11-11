# Make restrictions for the user
n = int(input("Introduce one number:"))
m = 4
print("{} / {} = {}".format(n, m, n/m))

# To avoid user incorrect inputs
try:
    n = int(input("Introduce one number:"))
    m = 4
    print("{} / {} = {}".format(n, m, n/m))
except:
    print("Unexpected error, introduce a number")

while(True):
    try:
        n = int(input("Introduce one number:"))
        m = 4
        print("{} / {} = {}".format(n, m, n/m))
        # Is important to break the iteration
        break
    except:
        print("Unexpected error, introduce a number")

while(True):
    try:
        n = int(input("Introduce one number:"))
        m = 4
        print("{} / {} = {}".format(n, m, n/m))
    except:
        print("Unexpected error, introduce a number")
    else:
        print("All the code is working correctly")
        # Is important to break the iteration
        break

while(True):
    try:
        n = int(input("Introduce one number:"))
        m = 4
        print("{} / {} = {}".format(n, m, n/m))
    except:
        print("Unexpected error, introduce a number")
    else:
        print("All the code is working correctly
    # This code will execute even if there is an error presented
    finally:
        print("End of the program")
