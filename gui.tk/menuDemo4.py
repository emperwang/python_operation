from tkinter import *


def callback():
    print("called the callback")

root = Tk()

# create menu
menu = Menu(root)
root.config(menu=menu)

fileMenu = Menu(menu)
menu.add_cascade(label='File', menu=fileMenu)

fileMenu.add_command(label="New", command=callback)
fileMenu.add_command(label="Open", command=callback)
fileMenu.add_separator()
fileMenu.add_command(label="exit", command=root.destroy)

helpMenu = Menu(menu)
menu.add_cascade(label="help", menu=helpMenu)

helpMenu.add_command(label="about", command=callback)

root.mainloop()