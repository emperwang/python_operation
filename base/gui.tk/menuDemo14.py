from tkinter import *


root = Tk()

def hello():
    print("hello")


menubar = Menu(root)

# create a pulldown menu
filemenu = Menu(menubar)
filemenu.add_command(label="Open", command=hello)
filemenu.add_command(label="Save", command=hello)
# filemenu.add_separator()
filemenu.add(SEPARATOR)
filemenu.add_command(label="Exit", command=root.quit)

# create a pulldown menu
editmenu = Menu(menubar)
editmenu.add_command(label="Cut", command=hello)
editmenu.add_command(label="Copy", command=hello)
editmenu.add_command(label="Paste", command=hello)

helpmenu = Menu(menubar)
helpmenu.add_command(label="About", command=hello)
helpmenu.add_command(label="Help", command=hello)

menubar.add(CASCADE, label="file", menu=filemenu)
menubar.add_cascade(label="edit", menu=editmenu)
menubar.add_cascade(label="help", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()