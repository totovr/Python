if True:
    print("The condition is met")
    print("Also this print is showed")

if False:
    print("The condition is met")
    print("Also this print is showed")

// Is the same has true
if not False:
    print("The condition is met")
    print("Also this print is showed")

a = 5
if a == 2:
    print("The value is 2")
if a == 5:
    print("The value is 5")

a = 5
b = 10
if a == 5:
    print("a value is", a)
    if b == 10:
        print("and b value is", b)

if a == 5 and b == 10:
    print("The value of a is 5 and b is 10")

n = 11
if n % 2 == 0:
    print(n, "is pair")
else:
    print(n, "is not pair")

command = "EXIT"
if command == "WELCOME":
    print("Welcome to the system")
elif command == "GRETTING":
    print("Hello, I hope that you are fine")
elif command == "EXIT":
    print("Closing the system")
else:
    print("This command is not recognized")

grade = float(input("Introduce a grade: "))
if grade >= 9:
    print("Excellent")
elif grade >= 7:
    print("Very good")
elif grade >= 6:
    print("Good")
else:
    print("Not enough")

if True:
    pass
