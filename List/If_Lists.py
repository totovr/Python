requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

# Insert and if in a list

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry we don't have this topping")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")
