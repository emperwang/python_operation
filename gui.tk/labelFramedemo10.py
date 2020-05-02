from tkinter import *

root = Tk()

group = LabelFrame(root, text="group", padx=5, pady=5)
group.pack()

w = Entry(group)
w.pack()

root.mainloop()