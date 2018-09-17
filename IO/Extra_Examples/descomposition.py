import sys

if len(sys.argv) == 2:
    n = int(sys.argv[1])
    if n < 0 or n > 9999:
        print("Introduce the correct statement: python3 descomposition.py [0-9999]")
    else:
        chain = str(n)
        long = len(chain)
        for i in range(long):
            print("{:04d}".format(int(chain[long - 1 - i]) * 10 ** i))
else:
    print("Introduce the correct statement: python3 descomposition.py [0-9999]")
