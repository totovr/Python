# Example 1
# This is an error
result = 10/0

try:
    result = 10/0
except ZeroDivisionError:
    print("A number can not be divide by 0")

# Example 2
# This is an error
list = [1, 2, 3, 4, 5]
list[10]

try:
    list = [1, 2, 3, 4, 5]
    list[10]
except IndexError:
    print("The index doesn't exist, use a number lower than", len(list))

# Example 3
# This is an error
colors = {'red': 'aka', 'green': 'mido', 'black': 'kuro'}
colors['white']

try:
    colors = {'red': 'aka', 'green': 'mido', 'black': 'kuro'}
    colors['white']
except KeyError:
    print("This key doesn't exist")

# Example 4
# This is an error
result = "20" + 15

try:
    result = "20" + 15
except TypeError:
    print("Is not possible to add one str and one int value")

# Example 5
list = [1, 5, -2]
def add(list, ele):
    try:
        if ele in list:
            raise ValueError
        else:
            list.append(ele)
    except ValueError:
        print("The value {} is already in the list".format(ele))
add(list, 10)
add(list, -2)
add(list, "Hello")

print(list)
