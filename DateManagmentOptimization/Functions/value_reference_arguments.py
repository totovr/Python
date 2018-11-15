# Reference by value, this will not affect the original number
def double_value(num):
    num *= 2
n = 10
double_value(n)
n

# Reference by "reference", this will affect the original number, is not possible
# to modify it directly in Python
def double_values(nums):
    for i, n in enumerate(nums):
        nums[i] *= 2

ns = [10, 50, 100]
double_values(ns)
ns

# Another way to implement the last syntaxis
def double_values(nums):
    for i in range(len(nums)):
        nums[i] *= 2

ns = [10, 50, 100]
double_values(ns)
ns

# With this way we can modify the value
def double_value(num):
    return num * 2
n = 10
n = double_value(n)
n

# With this techique is possible to create a copy of a colection
def double_values(nums):
    for i in range(len(nums)):
        nums[i] *= 2

ns = [10, 50, 100]
# This is the way to copy the colection
double_values(ns[:])
ns
