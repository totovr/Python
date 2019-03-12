import sqlite3

# Create the data base
connectionDB = sqlite3.connect("exampleDataBase.db")

# Create a seeker 
seekerConectionDB = connectionDB.cursor()

# Generate the table 
# seekerConectionDB.execute("CREATE TABLE users (name VARCHAR(100), age INTEGER, email VARCHAR(100))")

# Add one value
# seekerConectionDB.execute("INSERT INTO users VALUES ('Antonio', 27, 'tonovr@hiroshima-u.ac.jp')")

# Get all the data from the db
# seekerConectionDB.execute("SELECT * FROM users")
# Recover just one user, starting for the first one
# userRecover = seekerConectionDB.fetchone() # if we recover again this will move the seeker to the next position
# print(userRecover)
# print(userRecover[0]) # the userRecover will return a tuple

# Prepare a tuple to add more than one user in a massive form 
# users = [
#     ("Cindy", 29, "cindy@example.com"),
#     ("Alex", 13, "alex@example.com"),
#     ("Rocio", 50, "rocio@example.com")
# ]

# Now we will execute the next command to add many values
# seekerConectionDB.executemany("INSERT INTO users VALUES (?,?,?)", users)

# Recover all the users 
seekerConectionDB.execute("SELECT * FROM users")
# Load all the users in the variable users 
users = seekerConectionDB.fetchall()

for user in users:
    print("Name:", user[0], "- email:", user[2])

# Commit this values 
connectionDB.commit() # if we dont commit the changes this will not appear in the database

connectionDB.close()