import sqlite3

# conexionDB = sqlite3.connect("users.db")
# conexionDB = sqlite3.connect("products.db")

conexionDB = sqlite3.connect("users_autoincremental.db")
seekerDB = conexionDB.cursor()

# To create a table with primary key
# note if we create a table with a key value this value will not be able to be repated

# seekerDB.execute('''
#     CREATE TABLE users (
#         dni VARCHAR(9) PRIMARY KEY,
#         name VARCHAR(100),
#         age INTEGER,
#         email VARCHAR(100)
#     )
#     ''')

# users = [
#     ('11111111A', 'Antonio', 29, 'antonio@example.com'),
#     ('22222222B', 'Cindy', 29, 'cindy@example.com'),
#     ('33333333C', 'Alex', 13, 'alex@example.com'),
#     ('44444444C', 'Rocio', 50, 'rocio@example.com')
# ]

# To generate autoincremental primary keys

# seekerDB.execute('''
#     CREATE TABLE IF NOT EXISTS products (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name VARCHAR(100) NOT NULL,
#         brand VARCHAR(50) NOT NULL,
#         price FLOAT NOT NULL
#     )
#     ''')

# products = [
#     ('Keyboard', 'Logitech', 19.95),
#     ('Screen 19', 'LG', 89.95)
# ]

# the value null is for the incremental key
# seekerDB.executemany("INSERT INTO products VALUES (null,?,?,?)", products)

# seekerDB.execute("SELECT * FROM products") # Load the users
# products = seekerDB.fetchall() # save all the users in the variable

# for product in products:
#     print(product)


# Unique means that this value can not be repetead
# seekerDB.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         dni VARCHAR(9) UNIQUE, 
#         name VARCHAR(100),
#         age INTEGER, 
#         email VARCHAR(100)
#     )
#     ''')

# users = [
#     ('11111111A', 'Antonio', 29, 'antonio@example.com'),
#     ('22222222B', 'Cindy', 29, 'cindy@example.com'),
#     ('33333333C', 'Alex', 13, 'alex@example.com'),
#     ('44444444C', 'Rocio', 50, 'rocio@example.com')
# ]

# seekerDB.executemany("INSERT INTO users VALUES (null,?,?,?,?)", users)

# if we just want to add one user
seekerDB.execute("INSERT INTO users VALUES (null, '55555555D', 'David', '24', 'david@example.com')")

conexionDB.commit()
conexionDB.close()
