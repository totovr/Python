from tkinter import *

def select():
    monitor.config(text="{}".format(option.get()))

def reset():
    option.set(None)
    monitor.config(text="")

root = Tk()

option = IntVar()

Radiobutton(root, text="Option 1", variable=option, value=1, command=select).pack()
Radiobutton(root, text="Option 2", variable=option, value=2, command=select).pack()
Radiobutton(root, text="Option 3", variable=option, value=3, command=select).pack()

monitor = Label(root)
monitor.pack()

Button(root, text="Reset", command=reset).pack()

root.mainloop()