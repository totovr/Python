def sub(a, b):
    return a - b

sub(2, 1)

sub (b = 2, a = 1)

# Define null value
def sub(a = None, b = None):
    if a == None or b == None:
        print("Error you should introduce two numbers")
        return
    else:
        return a - b
sub()
