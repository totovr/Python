from tkinter import *
from tkinter import messagebox as MessageBox

root = Tk()


def test():
    # MessageBox.showinfo("Hello", "Hello world")

    # MessageBox.showwarning("Alert", "Just for admin")

    # MessageBox.showerror("Error", "Somethign wrong happened")

    # result = MessageBox.askquestion(
    #     "Log out", "Are you sure that you want to leave with out saving the file?")
    # if(result == "yes"): # no
    #     root.destroy()

    # result = MessageBox.askokcancel("Close", "Overwrite the file?")
    # result = MessageBox.askyesno("Close", "Are you sure to you want to close the file")
    # if(result):
    #     root.destroy()

    result = MessageBox.askretrycancel("Re-try", "Is not possible to connect")
    if(result):
        root.destroy()


Button(root, text="click", command=test).pack()

root.mainloop()
