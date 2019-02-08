from tkinter import *


def Sum():
    if(n1.get().isdigit() and n2.get().isdigit()):
        result.set(float(n1.get()) + float(n2.get()))
    Erase()

def Sub():
    if(n1.get().isdigit() and n2.get().isdigit()):
        result.set(float(n1.get()) - float(n2.get()))
    Erase()

def Mul():
    if(n1.get().isdigit() and n2.get().isdigit()):
        result.set(float(n1.get()) * float(n2.get()))
    Erase()

def Erase():
    n1.set("")
    n2.set("")

# root config
root = Tk()
root.title("Calculator")
root.config(bd=15)
root.resizable(0, 0) 

n1 = StringVar()
n2 = StringVar()
result = StringVar()

Label(root, text="Number 1").grid(row=0,column=1)
Entry(root, justify="center", textvariable=n1).grid(row=1,column=1)

Label(root, text="Number 2").grid(row=2,column=1)
Entry(root, justify="center", textvariable=n2).grid(row=3,column=1)

Label(root, text="Result").grid(row=4,column=1)
Entry(root, justify="center", textvariable=result, state=DISABLED).grid(row=5,column=1)

Label(root, text="").grid(row=6,column=0)# separate

Button(root, text="Sum", command=Sum).grid(row=7,column=0)
Button(root, text="Sub", command=Sub).grid(row=7,column=1)
Button(root, text="Product", command=Mul).grid(row=7,column=2)

root.mainloop()
