from tkinter import *

def new_file():
    messageDisplay.set("New file")

def open_file():
    messageDisplay.set("Open file")

def save_file():
    messageDisplay.set("Save file")

def save_file_as():
    messageDisplay.set("Save file as")

root = Tk()
root.title("Editor")

# Create the menu in root
menubar = Menu(root)

# Create the menu options
filemenu = Menu(menubar, tearoff=0)
# Create the submenus of filemenu
filemenu.add_command(label="New", command=new_file)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_file)
filemenu.add_command(label="Save as", command=save_file_as)
filemenu.add_separator() # this is a simple separator
filemenu.add_command(label="Close", command=root.quit)
# add to main menu 
menubar.add_cascade(label="File", menu=filemenu)

# Central text box
centralText = Text(root, padx=6, pady=4, bd=0, font=("Consolas", 12))
# centralText.config(padx=6, pady=4, bd=0, font=("Consolas", 12))
centralText.pack(fill='both', expand=1)

# monitor down
messageDisplay = StringVar()
messageDisplay.set('Write something')
statusLabel = Label(root, textvar=messageDisplay, justify='left')
statusLabel.pack(side='left')

# add menu to root
root.config(menu=menubar)

root.mainloop()