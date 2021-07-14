from tkinter import *

root = Tk()

#w = Spinbox(root, from_=0, to=10)
w = Spinbox(root, values=(2, 4, 6, 8, 10))
w.pack()


root.mainloop()