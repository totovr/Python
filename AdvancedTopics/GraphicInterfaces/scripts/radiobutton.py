from tkinter import *

def Select():
    monitor.config(text="{}".format(option.get()))

def Reset():
    option.set(None)
    monitor.config(text="")

root = Tk()

option = IntVar()

Radiobutton(root, text="Option 1", variable=option, value=1, command=Select).pack()
Radiobutton(root, text="Option 2", variable=option, value=2, command=Select).pack()
Radiobutton(root, text="Option 3", variable=option, value=3, command=Select).pack()

monitor = Label(root)
monitor.pack()

Button(root, text="Reset", command=Reset).pack()

root.mainloop()