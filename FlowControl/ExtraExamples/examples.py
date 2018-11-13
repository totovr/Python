# First
while(True):
    n1 = float(input("Introduce the first number"))
    n2 = float(input("Introduce the second number"))
    print("""
        What do you want to do:
        1) Plus two numbers
        2) Substract two numbers
        3) Multiply two numbers""")
    inputCommand = float(input())
    if (inputCommand == 1):
        print("The result is", n1+n2)
    elif (inputCommand == 2):
        print("The result is", n1-n2)
    elif (inputCommand == 3):
        print("The result is", n1 * n2)
    else:
        print("Unkown command")
        break

# Second
inputCommand = 0
print("Introduce an impair number")
while inputCommand % 2 == 0:
    inputCommand = int(input("Introduce an impair number: "))

# Third
# Sum of all the number since 0 until 100
for i in range(0,101,2):
    print(i)

# Fourth
numbers = int(input("How many numbers do you want to introduce: "))
for x in range(numbers):
    sum = float(input("Introduce a number"))
    sum += sum
average = sum/numbers
print("The total numbers introduced were ",numbers,", the total sum of this numbers were ",sum,", and the average was ", average)

# Fifth
print(list(range(0,11)))
print(list(range(-10,1)))
print(list(range(0,21)))
print(list(range(0,21,2)))
print(list(range(-19,1,2)))
print(list(range(0,51,5)))

# Seventh
list1 = ('H','e','l','l','o')
list2 = ('h','o','l','a')
list3 = []
for letter in list1:
    if letter in list2 and letter not in list3:
        list3.append(letter)
print(list3)
