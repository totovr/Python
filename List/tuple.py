# Are the same as a list but this ones can't be modified, use () instead of []

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Although you can’t modify a tuple, you can assign a new value to a variable that holds a tuple. So if we wanted to change our dimensions, we could redefine the entire tuple:

dimensions = (400, 100)
print("Modified dimensions:")
for dimension in dimensions:
    print(dimension)
    
