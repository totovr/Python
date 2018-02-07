motorcycles = ['Honda', 'Yamaha', 'Suzuki']
print(motorcycles)
# change the value 0
motorcycles[0] = "Ducati"
print(motorcycles)
# The method append add a value to the list in the last possition
motorcycles = ['Honda', 'Yamaha', 'Suzuki']
print(motorcycles)
motorcycles.append('Ducati')
print(motorcycles)
# Insert method, put the value in the position that we indicate and move the last value to the right
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)
# Removing elements of the list "del" function
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
# Pop method delate the last value of the list but lets you use it in the future
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
# 'susuki' was removed and saved it in popped_motorcycle
print(motorcycles)
print(popped_motorcycle)
# pop() also can remove an item in a list at any position by including the index
# of the item you want to remove in parentheses
motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop(1)
print('My first motorcycle was a ' + last_owned.title() + '.')
# Sometimes you won’t know the position of the value you want to remove
# from a list. If you only know the value of the item you want to remove, you
# can use the remove() method.
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.remove('suzuki')
print(motorcycles)
