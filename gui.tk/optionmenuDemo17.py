from tkinter import *

root = Tk()
root.geometry("500x400+200+200")
strvar = StringVar()
strvar.set("one")

w = OptionMenu(root, strvar, "one", "one", "two","three", "five")
w.pack()

root.mainloop()