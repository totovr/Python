# Do some operations 
def sumS(a, b):
    try:
        r = a + b
    except TypeError:
        print("Please type a number")
    else:
        return r

def sub(a, b):
    try:
        r = a - b
    except TypeError:
        print("Please type a number")
    else:
        return r

def mul(a, b):
    try:
        r = a * b
    except TypeError:
        print("Please type a number")
    else:
        return r

def divS(a, b):
    try:
        r = a / b
    except TypeError:
        print("Please type a number")
    except ZeroDivisionError:
        print("First number must not be 0")
    else:
        return r