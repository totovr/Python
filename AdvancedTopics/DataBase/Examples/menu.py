import sqlite3
from tkinter import * 

# Config of the root
root = Tk()
root.title("Restaurant el Cielo")
root.resizable(0,0)
root.config(bd=25, relief="sunken")

Label(root, text="   El cielo restaurant   ", fg="darkblue", font=("Times New Roman", 28, "bold italic")).pack()
Label(root, text="   Menú del día   ", fg="blue", font=("Times New Roman", 24, "bold italic")).pack()

# Separate titles and categories with this label
Label(root, text="").pack()

# Connect to the data base
conexionDB = sqlite3.connect("restaurant.db")
seekerDB = conexionDB.cursor()

# Search for the categories and dishes
categories = seekerDB.execute("SELECT * FROM category").fetchall()

for category in categories:
    # Add the categories
    Label(root, text=category[1], fg="white", font=("Times New Roman", 20, "bold italic")).pack()
    # Get all the dishes  
    dishDB = conexionDB.execute("SELECT * FROM dish WHERE category_id={}".format(category[0])).fetchall()
    for dish in dishDB:
        Label(root, text=dish[1], fg="gray", font=("Verdana", 20, "italic")).pack()

conexionDB.close()

# Show a label with the price
Label(root, text="60 pesos (IVA inclu) ", fg="darkblue", font=("Times New Roman", 20, "bold italic")).pack(side="right")

root.mainloop()