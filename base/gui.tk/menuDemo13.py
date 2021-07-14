from tkinter import *

root = Tk()

def hello():
    print("hello")

menu = Menu(root)
menu.add_command(label="hello", command=hello)
menu.add(COMMAND, label="quit", command=root.destroy)

root.config(menu=menu)


root.mainloop()