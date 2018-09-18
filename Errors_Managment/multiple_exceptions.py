# Generic error exception
try:
    n = input("Introduce one number: ")
    5 / n
# With this code we can show which kind of error is presented
except Exception as e:
    print(type(e).__name__)

# Is possible to add exceptions
try:
    n = float(input("Introduce one number: "))
    5 / n
except TypeError:
    print("Is not possible to divide a number with a chain")
except ValueError:
    print("You must introduce a number chain")
except ZeroDivisionError:
    print("Is not possible to divide 0 with a number")
# Generic error exception
except Exception as e:
    print(type(e).__name__)
