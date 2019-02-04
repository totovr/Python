from tkinter import *

# Root configuration
root = Tk()

"""
# Frame configuration
# frame = Frame(root, width=480, height=320)
# frame.pack()

# label = Label(root, text="Hello world")
# label.place(x=0, y=0) # where is going to be placed 
# label.pack()

# Dinamyc variables
text = StringVar()
text.set("A new text")

Label(root, text="Hello world").pack(anchor="nw") # if we dont use the label variable
label = Label(root, text="how are you?")
label.pack(anchor="center")
Label(root, text="I hope good").pack(anchor="se")

label.config(bg="green", fg="blue", font=("Verdana", 24))
label.config(textvariable = text)

"""

image = PhotoImage(file="image.gif")
Label(root, image=image, bd=0).pack()

# Bucle of the app
root.mainloop()