from tkinter import * 

# root config
root = Tk()

root.title("Name")     # Window name 
root.resizable(0, 0)         # Window will not resize

label = Label(root, text="Name")
label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
# grid will adjust better the text
# sticky will justify the text of the label in the gird
# padx/y will provide distance from the root
entry = Entry(root)
entry.grid(row=0, column=1, padx=5, pady=5)
entry.config(justify="right", state="normal")
# justify the enter text
# state will enable or disabled the text

label2 = Label(root, text="Password")
label2.grid(row=1, column=0, sticky="w", padx=5, pady=5)

entry2 = Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)
entry2.config(justify="center", show='*')
# show will be use if we dont want to display the data

# bucle of the app
root.mainloop()