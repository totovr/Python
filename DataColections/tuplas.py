 tupla = (100, "Hello", [1, 2, 3, 4], -50)
 tupla

tupla[3]
tupla[2][3]

# One tuple can not be modified
tupla[0] = 50

len(tupla)
len(tupla[2])

# . index can be used to find one element and know it position
tupla.index(100)
tupla.index("Hello")

# .count provide the number of elements that are in the tuple
tupla.count(100)

# .append() will give an error
tupla.append(100)
