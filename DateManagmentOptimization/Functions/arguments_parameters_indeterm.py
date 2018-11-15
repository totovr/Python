# Examples with indeterminated position

def indeterminated_position(*args):
    for i in args:
        print(i)
indeterminated_position(5, "hello", [1, 2, 3, 4, 5])

# Examples indeterminated name
def indeterminated_name(**kwargs):
    print(kwargs)
indeterminated_name(n = 5, c = "hello", l = [1, 2, 3, 4, 5])

def indeterminated_name(**kwargs):
    for kwarg in kwargs:
        print(kwarg)
indeterminated_name(n = 5, c = "hello", l = [1, 2, 3, 4, 5])

def indeterminated_name(**kwargs):
    for kwarg in kwargs:
        print(kwarg, " ", kwargs[kwarg])
indeterminated_name(n = 5, c = "hello", l = [1, 2, 3, 4, 5])


# Example mixing position and names
def super_function(*args, **kwargs):
    t = 0
    for arg in args:
        t += arg
    print("The total is: ", t)
    for kwarg in kwargs:
        print(kwarg, " ", kwargs[kwarg])

super_function(10, 50, -1, 1.56, 10, 20, 300, name = "Tono", age = "26")
