 def something(n = None):
     if n is None:
         print("Is not possible to use a null value")
something()
something("Hello")

# Summon an exception
def something(n = None):
    if n is None:
        raise ValueError("Is not possible to use a null value")
something()

# Other example
def something(n = None):
    try:
        if n is None:
            raise ValueError("Is not possible to use a null value")
    except ValueError:
        print("Is not possible to use a null valueee")


something()
