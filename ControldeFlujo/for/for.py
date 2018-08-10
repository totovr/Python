numbers = [1,2,3,4,5,6,7,8,9,10]
index = 0
while(index < len(numbers)):
    print(numbers[index])
    index+=1

numbers = [1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    print(numbers)

for number in numbers:
    number *= 10
numbers

index = 0
numbers = [1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    numbers[index] *= 10
    index+=1
numbers

numbers = [1,2,3,4,5,6,7,8,9,10]
for index, number in enumerate(numbers):
    numbers[index] *= 10
numbers

chain = "Hello friends"
for character in chain:
    print(character)

// This will be an error
chain = "Hello friends"
for i, c in enumerate(chain):
    chain[i] = "*"

chain2 = ""
for character in chain:
    chain2 += "*"
chain
chain2

for i in range(10):
    print(i)
range(10)

list(range(10))
