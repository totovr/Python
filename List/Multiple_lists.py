available_tacos = ['pastor', 'bistec', 'chorizo']
requested_tacos = ['tripa', 'pastor', 'arrachera']

for requested_taco in requested_tacos:
    if requested_taco in available_tacos:
        print("Adding taco of " + requested_taco + ".")
    else:
        print("Sorry, we don't have " + requested_taco + ".")
