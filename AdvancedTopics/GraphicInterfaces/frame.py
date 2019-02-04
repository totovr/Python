from tkinter import *

root = Tk()

root.title("Hello world")
root.resizable(1,1) # 1,1 mean yes
root.iconbitmap('hello.ico')

# This is form the frame
frame = Frame(root, width=480, height = 320)
# frame.pack(side="bottom", anchor="e") # package in the own frame
frame.pack(fill='both', expand=1) # x, y, both
frame.config(cursor="pirate") # For the cursor
frame.config(bg="lightblue") # For the color of the background
frame.config(bd=25) # add a border of 25 pixels
frame.config(relief="sunken") # add a style to the frame

# This is for the root
root.config(cursor="arrow") # For the cursor
root.config(bg="blue") # For the color of the background
root.config(bd=15) # add a border of 25 pixels
root.config(relief="ridge") # add a style to the frame

# Alway down of everything
root.mainloop ()