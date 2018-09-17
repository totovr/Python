def test():
    return "One chain returned"
    print("Another text")

test()
print(test())

c = test()
print(c)

# This will be an error, we can not sum an str and one int
c = test() + 10

def test():
    return [1, 2, 3, 4, 5]
print(test())

# Is possible to use slicing method
print(test()[-1])
l = test()
l[-1]

def test():
    return "hello", 20, [1, 2, 3]
test()

c, n , l = test()
c
n
l
