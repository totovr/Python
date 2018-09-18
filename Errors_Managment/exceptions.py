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
