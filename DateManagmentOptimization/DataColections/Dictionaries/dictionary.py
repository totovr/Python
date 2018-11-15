# Always a key-value
# Just can not have a key name repeted

exampleDic = {}
exampleDic

type(exampleDic)

colors = {'yellow': 'amarillo', 'blue': 'azul', 'green': 'verde'}
colors

# To access to the elements of the dictionary
colors['blue']
colors['yellow']

numbers = {10: 'ten', 20: 'twenty'}
numbers[10]

# To modify the registers of the dictionary
colors['yellow'] = 'white'
colors

# To delate
del(colors['yellow'])
colors

# To modify the dictionary values again
ages = {'Antonio': 26, 'Cindy': 29, 'Alex': 12}
ages
ages['Antonio'] += 1
ages

ages['Antonio'] + ages['Cindy']

# To acces key
for age in ages:
    print(age)

# To access value
for key in ages:
    print(ages[key])

# To acces key and value at the same time
for key in ages:
    print(key, ages[key])

# Another way
for k, v in ages.items():
    print(k, v)

# Example
characters = []

p = {'Name': 'Gandalf', 'Class': 'Wizard', 'Race': 'Human'}
characters.append(p)
characters

p = {'Name': 'Legolas', 'Class': 'Archer', 'Race': 'Elf'}
characters.append(p)
characters

p = {'Name': 'Gimli', 'Class': 'Warrior', 'Race': 'Dwarf'}
characters.append(p)
characters

for p in characters:
    print(p['Name'], p['Class'], p['Race'])
