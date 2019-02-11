from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

root = Tk()


def test():
    # Advanced

    # color = ColorChooser.askcolor(title="Choose a color")
    # print(color)

    # this return a route
    # route = FileDialog.askopenfile(
    #     title="Open a file", initialdir="/Users/bsys", filetypes=(("Text file", "*.txt"), ("Advanced files", "*.py"), ("All the possible files files", "*.*")))
    # print(route)

    # this return a file
    # is the same as open('route', 'w')
    fileReturned = FileDialog.asksaveasfile(title="Save file", mode='w', defaultextension = ".txt")
    if fileReturned is not None:
        fileReturned.write("Hello!, I will write something")
        fileReturned.close

Button(root, text="click", command=test).pack()

root.mainloop()
