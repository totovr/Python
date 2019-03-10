from tkinter import *
from tkinter import filedialog as FileDialog
from io import open

mainPath = ""


def new_file():
    global fileMainPath
    messageDisplay.set("New file")
    fileMainPath = ""
    # erase from the first character until the end
    centralText.delete(1.0, "end")


def open_file():
    global fileMainPath
    messageDisplay.set("Open file")

    fileMainPath = FileDialog.askopenfilename(
        initialdir='.',
        filetypes=(
            ("Text files", "*.txt"),
        ),
        title="Open a text file"
    )

    # Si la ruta es válida abrimos el contenido en lectura
    if fileMainPath != "":
        currentFile = open(fileMainPath, 'r')
        currentFileContent = currentFile.read()
        centralText.delete(1.0, 'end')           # We check that if is empty
        # Insert the open script content
        centralText.insert('insert', currentFileContent)
        currentFile.close()                    # Close the file
        root.title(fileMainPath + " - Tono editor")  # Change the title


def save_file():
    global fileMainPath
    messageDisplay.set("Save file")

    if fileMainPath != "":
        # Get the text that the use wrote but with no the return of line
        centralTextContent = centralText.get(1.0, 'end-1c')
        currentFile = open(fileMainPath, 'w+')         # Write and read
        currentFile.write(centralTextContent)           # Write the text
        currentFile.close()
        messageDisplay.set('File saved correctly')
    else:
        save_file_as()  # If the file does not exist


def save_file_as():
    global fileMainPath
    messageDisplay.set("Save file as")

    currentFile = FileDialog.asksaveasfile(title="Save file", mode='w',
                                           defaultextension=".txt")

    if currentFile is not None:
        fileMainPath = currentFile.name  # The atribute name is the route if is open
        centralTextContent = centralText.get(1.0, 'end-1c')
        currentFile = open(fileMainPath, 'w+')
        currentFile.write(centralTextContent)
        currentFile.close()
        messageDisplay.set('File saved correctly')
    else:
        messageDisplay.set('File was not save')
        fileMainPath = ""


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
filemenu.add_separator()  # this is a simple separator
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
