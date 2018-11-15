import random
import math

def read_number(ini, end, message):
    
    while(True):
        try:
            value = int(input(message)) # We can check if the user introduce an int value 
        except Exception as e:
            print("A " + type(e).__name__ + " has been generated")
        else:
            if value >= ini and value <= end:
                break
    return value

def generator():
    
    numbers = read_number(1, 20, "How many numbers do you want to generate from [1] until [20]? ")
    mode = read_number(1, 3, "How do you want to round the numbers? [1] Upwards [2] Downwards [3] Normal: ")

    l = []

    for n in range(numbers):
        r = random.uniform(0,100)
        if mode == 1:
            print("{} => {}".format(r, math.ceil(r)) )
            r = math.ceil(r)
        elif mode == 2:
            print("{} => {}".format(r, math.floor(r)) )
            r = math.floor(r)
        else:
            print("{} => {}".format(r, round(r)) )
            r = round(r)
        l.append(r)
    
    return l

w = generator()
print(w)



