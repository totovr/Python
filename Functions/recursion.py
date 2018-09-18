# Example 1
def count_down(num):
    num -= 1
    if num > 0:
        print(num)
        count_down(num)
    else:
        print("Boom")
    print("The function is over", num)

count_down(5)

# Example 2
def factorial(num):
    if num > 1:
        num = num * factorial(num - 1)
    return num

factorial(5)

# Example 3
def factorial(num):
    print("Initial value: ", num)
    if num > 1:
        num = num * factorial(num - 1)
    print("Final value: ", num)
    return num

factorial(5)
