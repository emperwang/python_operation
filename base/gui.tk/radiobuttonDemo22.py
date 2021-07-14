from tkinter import *

root = Tk()

MODES = [
    ("Monochrome", "1"),
    ("Grayscale", "L"),
    ("True color", "RGB"),
    ("Color separation", "CMYK")
]

v = StringVar()
v.set("L")

for text, mode in MODES:
    b = Radiobutton(root, text=text, variable=v, value=mode)
    b.pack(anchor=W)


root.mainloop()