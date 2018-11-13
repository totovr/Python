import sys

# First position if for the script
if len(sys.argv) == 3:
    rows = int(sys.argv[1])
    columns = int(sys.argv[2])

    if rows < 1 or rows > 9 or columns < 1 or columns > 9:
        print("ERROR, introduce the correct statments")
        print("Example: write_lines.py [1-9] [1-9]")
    else:
        for x in range(rows):
            print("")
            for y in range(columns):
                print(' * ', end="")

else:
    print("ERROR, introduce the correct statments")
    print("Example: write_lines.py [1-9] [1-9]")
