numbers = list(range(1,6))
print(numbers)

#Skip values, in this case 2
even_numbers = list(range(2,11,2))
print(even_numbers)

#Add values to one list using range
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

#Calculate the value inside of append
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)
