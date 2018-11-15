import sys
# First position if for the script
if len(sys.argv) == 3:
    # Position for text
    text = sys.argv[1]
    # Number of repetitions
    repetitions = int(sys.argv[2])
    for r in range(repetitions):
        print(text)
else:
    print("ERROR, introduce the correct statments")
    print("Example: write_lines.py 'text' 5")

# NEVER send '' in the command line, use always ""
