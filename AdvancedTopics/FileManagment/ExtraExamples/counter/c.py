from io import open
import sys

file = open("counter.txt", "a+")  # Create the file in case that doesn't exist
file.seek(0)  # return to the 0 index

content = file.readline()  # try to read the data

if len(content) == 0:  # if there is no content by default a 0 will be write
    content = '0'
    file.write(content)

file.close()

counter = int(content)

try:
    # lets read the user input
    if len(sys.argv) == 2:
        if sys.argv[1] == "inc":
            counter += 1
        elif sys.argv[1] == "dec":
            counter -= 1
    
    print(counter)
    counter = str(counter)
    file = open("counter.txt", "w", encoding="utf8")  # remove everything and write the new data
    file.write((counter))
    file.close()
    
except:
     print("Something bad happend")
