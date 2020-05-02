from tkinter import *

root = Tk()

v = IntVar()

Radiobutton(root, text="one", variable=v, value=1) \
    .pack(anchor=W)
Radiobutton(root, text="two", variable=v, value=2)\
    .pack(anchor=W)

root.mainloop()