from tkinter import *

root = Tk()
root.title("scrollbar")
root.geometry("500x400+200+200")
frame = Frame(root, width=200, height=200)
scollbar = Scrollbar(frame, orien=VERTICAL)
listbox = Listbox(frame, yscrollcommand=scollbar.set, height=5)
scollbar.config(command=listbox.yview)



for item in ["one","two","three","four","five","six","seven"]:
    listbox.insert(END, item)

listbox.activate(0)
frame.pack()
scollbar.pack(side=RIGHT, fill=Y)
listbox.pack(side=LEFT, fill=BOTH, expand=1)



root.mainloop()