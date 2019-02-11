from tkinter import *

def select():
    cadena = ""
    if (milk.get()):
        cadena += "With milk"
    else:
        cadena += "Without milk"

    if (sugar.get()):
        cadena += " and sugar"
    else:
        cadena += " and without sugar"

    monitor.config(text=cadena)

# root config 

root = Tk()
root.title("Cafeteria")
root.config(bd=15)

milk = IntVar()
sugar = IntVar()

image = PhotoImage(file="image.gif")
Label(root, image=image).pack(side="left")

frame = Frame(root)
frame.pack(side="left")

Label(frame, text="¿How do you want your coffe?").pack(anchor="w")
Checkbutton(frame, text="With milk", variable=milk, onvalue=1, 
            offvalue=0, command=select).pack(anchor="w")
Checkbutton(frame, text="With sugar", variable=sugar, onvalue=1, 
            offvalue=0, command=select).pack(anchor="w")

monitor = Label(frame)
monitor.pack()

root.mainloop()