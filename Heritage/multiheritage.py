class A:
    def __init__(self):
        print("I am the class A")
    def a(self):
        print("I am a method of the class A")

class B:
    def __init__(self):
        print("I am the class B")
    def b(self):
        print("I am a method of the class B")

# Python take in to account the first class of the left
# class C(A,B):
#    pass

# c = C()

class C(A,B):
    def c(self):
        print("This is a method of the C class")

c = C()
c.a()
c.b()
c.c()
