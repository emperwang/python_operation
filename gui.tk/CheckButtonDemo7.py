from tkinter import *

root = Tk()

var = IntVar()
def printVar():
    print(var.get())

c = Checkbutton(root, text="expand", variable=var, command=printVar)
c.pack()


root.mainloop()