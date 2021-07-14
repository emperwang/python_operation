from tkinter import *

root = Tk()

counter = 0

def update(menu):
    global counter
    counter += 1
    menu.entryconfig(1, label=str(counter))

menubar = Menu(root)
menu = Menu(menubar, postcommand=lambda : update(menu))
menu.add_command(label=str(counter))
menu.add_command(label="exit", command=root.quit)

menubar.add_cascade(label="text", menu=menu)

root.config(menu=menubar)
root.mainloop()