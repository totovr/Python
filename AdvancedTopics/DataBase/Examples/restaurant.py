import sqlite3

def create_bd():

    # Create the data base if is not created and connect to it
    conexionDB = sqlite3.connect("restaurant.db")

    # Generate the cursor
    seekerDB = conexionDB.cursor()

    # Create the first table 
    seekerDB.execute('''
        CREATE TABLE IF NOT EXISTS category (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) UNIQUE NOT NULL
        )
        ''')

    # Create the second table 
    seekerDB.execute('''
        CREATE TABLE IF NOT EXISTS dish (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) UNIQUE NOT NULL,
            category_id INTEGER NOT NULL,
            FOREIGN KEY (category_id) REFERENCES category(id)
        )
        ''')

    conexionDB.commit()
    conexionDB.close()

def add_category():

    category = input("\nName of the new category? \n > ")
    
    conexionDB = sqlite3.connect("restaurant.db")
    seekerDB = conexionDB.cursor()
    try:
        seekerDB.execute("INSERT INTO category VALUES (null, '{}')".format(category) )
    except sqlite3.IntegrityError:
        print("\nThe category '{}' already exist.".format(category))
    else:
        print("\nThe category '{}' has been created correctly".format(category))

    conexionDB.commit()
    conexionDB.close()

def add_dish():

    conexionDB = sqlite3.connect("restaurant.db")
    seekerDB = conexionDB.cursor()

    # Get the data of the categories 
    categories = seekerDB.execute("SELECT * FROM category")
    print("Select one category to add a dish")

    for category in categories:
        print("[{}] {}".format(category[0], category[1]))

    # Select the category
    category_user = int(input("> "))

    # add the dish
    dish_user = input("Name of the new dish: \n>")

    try:
        seekerDB.execute("INSERT INTO dish VALUES (null, '{}', {})".format(
            dish_user, category_user) )
    except sqlite3.IntegrityError:
        print("The dish '{}' already exist.".format(dish_user))
    else:
        print("The dish '{}' has been created correctly.".format(dish_user))
    
    conexionDB.commit()
    conexionDB.close()

def show_menu():
    conexionDB = sqlite3.connect("restaurant.db")
    seekerDB = conexionDB.cursor()

    categories = seekerDB.execute("SELECT * FROM category").fetchall()

    for category in categories:
        print("{}:".format(category[1]))
        dishDB = conexionDB.execute("SELECT * FROM dish WHERE category_id={}".format(category[0])).fetchall()
        for dish in dishDB:
            print("\t{}".format(dish[1]))

    conexionDB.close()

# Create the data base
create_bd()

# Options of the menu 
while True:
    
    print("\n Welcome to the restaurant manager")
    
    option = input(
        "\nIntroduce one option:" \
        "\n[1] Add one category" \
        "\n[2] Add a dish" \
        "\n[3] Show the menu" \
        "\n[4] Quit the program\n\n> ")
    
    if option == "1":
        add_category() 
    elif option == "2":
        add_dish()
    elif option == "3":
        show_menu()
    elif option == "4":
        print("\n See you later!")
        break
    else:
        print("\n Choose the correct option")