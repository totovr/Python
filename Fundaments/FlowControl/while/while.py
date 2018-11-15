c = 0
while c <= 5:
    c+=1
    print("c value", c)

c = 0
while c <= 5:
    c+=1
    print("c value", c)
else:
    print("The iteration has been completed and the value of c is", c)

c = 0
while c <= 5:
    c+=1
    if (c == 4):
        print("Break the bucle when the value is", c)
        break
    print("c value", c)
else:
    print("The iteration has been completed and the value of c is", c)

c = 0
while c <= 5:
    c+=1
    if (c == 3 or c == 4):
        #print("c value", c)
        # jump the iteration with this values
        continue
    print("c value", c)
else:
    print("The iteration has been completed and the value of c is", c)

# This is an example of an interactive menu
print("Welcome to this interactive menu")
while(True):
    print("""What do you want to do? Type an option
    1) Grettings
    2) Plus some numbers
    3) Exit""")
    option = input()
    if option == '1':
        print("Hello, how are you?")
    elif option == '2':
        n1 = float(input("Introduce the first number: "))
        n2 = float(input("Introduce the second number: "))
        print("The result is: ", n1+n2)
    elif option == '3':
        print("See you next time")
        break
    else:
        print("Unkown command, please type again")
