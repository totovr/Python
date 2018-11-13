# First example
users = {"Tono", "Alex", "Cindy", "David", "Marcus"}
admnistrators = {"David", "Tono"}
admnistrators.discard("David")
admnistrators
admnistrators.add("Marcus")
admnistrators

for user in users:
    if user in admnistrators:
        print(user, "is admin")
    else:
        print(user, "is not admin")

# Second example
cavalier = {'life': 2, 'attack': 2, 'defense': 2, 'range': 2}
warrior = {'life': 2, 'attack': 2, 'defense': 2, 'range': 2}
archer = {'life': 2, 'attack': 2, 'defense': 2, 'range': 2}

cavalier['life'] = warrior['life'] * 2
cavalier['defense'] = warrior['defense'] * 2

warrior['attack'] = cavalier['attack'] * 2
warrior['range'] = cavalier['range'] * 2

archer['life'] = warrior['life']
archer['attack'] = warrior['attack']
archer['defense'] = warrior['defense'] / 2
archer['range'] = warrior['range'] * 2

print("Cavalier:\t", cavalier)
print("Warrior:\t", warrior)
print("Archer:\t", archer)

# Third example
tasks = [
    [6, 'Distribution'],
    [2, 'Design'],
    [1, 'Conception'],
    [7, 'Maintenance'],
    [4, 'Production'],
    [3, 'Planification'],
    [5, 'Probes']
    ]

print("==Tasks with no order==")
for task in tasks:
    print(task[0], task[1])

from collections import deque

tasks.sort()
tasks

tail = deque()
for task in tasks:
    tail.append(task[1])

print("==Tasks with order==")
for task in tail:
    print(task)
