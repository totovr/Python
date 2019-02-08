from tkinter import *

# config root
root = Tk()

text = Text(root)
text.pack()
text.config(width=30, height=10, font=("Consolas", 12), padx=5, pady=5, selectbackground="red")
# width and height read number of characters

root.mainloop()