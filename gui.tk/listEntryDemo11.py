from tkinter import *

root = Tk()
root.title("listbox")
root.geometry("400x500+200+200")

def printselect(sel):
    print(sel.curselection())
    print(sel.get(sel.curselection()))


listbox = Listbox(root)
listbox.pack()

listbox.insert(END, "A list entry")

for item in ["one", "two", "three", "four"]:
    listbox.insert(END, item)

Button(root, text="sels", command=lambda : printselect(listbox))\
    .pack()

root.mainloop()