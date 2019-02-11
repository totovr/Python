from tkinter import * 

root = Tk()

menubar = Menu(root)
root.config(menu=menubar) # asign to the base, this is the menu

# sub menus
filemenu = Menu(menubar, tearoff=0) 
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_command(label="Close")
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut")
editmenu.add_command(label="Copy")
editmenu.add_command(label="Paste")

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help")
helpmenu.add_separator()
helpmenu.add_command(label="Information")

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Edit", menu=editmenu)
menubar.add_cascade(label="Help", menu=helpmenu)

root.mainloop()