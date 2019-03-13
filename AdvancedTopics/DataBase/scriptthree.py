import sqlite3

conexionDB = sqlite3.connect("users_autoincremental.db")
seekerDB = conexionDB.cursor()

# If we add WHERE and the variable we can get the user that we indicate
# seekerDB.execute("SELECT * FROM users WHERE dni='22222222B'") 
# If two data has the same value it will pick the first one in the list for example if two users has the same age

# But is possible to get all the variables with the common value with 
# users = seekerDB.fetchall()
# print(users)

# If we want to modify one value
# seekerDB.execute("UPDATE users SET name='Antonio Vega' WHERE dni='11111111A'")

# If we want to modify many values
# seekerDB.execute("UPDATE users SET name='Antonio Vega', age=26 WHERE dni='11111111A'")

# If we dont use WHERE it will update all the users

# If we want to delate an user
# seekerDB.execute("DELETE FROM users WHERE dni='11111111A'")
# seekerDB.execute("DELETE FROM users")

# If we want to delate all the users


# if we want to modify many values 


user = seekerDB.fetchone()
print(user) 

conexionDB.commit()
conexionDB.close()