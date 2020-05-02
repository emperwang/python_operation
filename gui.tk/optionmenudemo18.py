from tkinter import *

root = Tk()
root.geometry("500x400+200+200")
strvar = StringVar()
strvar.set("one")

w = OptionMenu(root, strvar, "one", "two", "three", "five")
w.pack()

def getsel():
    print("select:{}".format(strvar.get()))

Button(root, text="ok", command=getsel) \
    .pack()


root.mainloop()