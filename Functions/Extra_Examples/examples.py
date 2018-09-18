# Example 1
def rectangle_area(a, b):
    return a * b

rectangle_area(15, 10)

# Example 2
import math

def circle_area(rad):
    return (rad ** 2) * math.pi

circle_area(5)

# Example 3
def relation(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0

relation(5, 10)
relation(10, 5)
relation(5, 5)

# Example 4
def intermediate(a, b):
    return (a + b) / 2
intermediate(-12, 24)

# Example 5
def cut(n, l, h):
    if n < l:
        print(l)
    elif n > h:
        print(h)
    else:
        print(n)

cut(15, 0, 10)

# Example 6
def separate(li):
    li.sort()
    pair = []
    impair = []
    for i in li:
        if i % 2 != 0:
            impair.append(i)
        else:
            pair.append(i)
    return pair, impair

num = [-12, 84, 13, 20, -33, 101, 9]
pair, impair = separate(num)
print(pair)
print(impair)
