from tkinter import  *

root = Tk()

def hello():
    print("hello")

# create a popup menu
menu = Menu(root)
menu.add_command(label="Undo", command=hello)
menu.add_command(label="Redo", command=hello)

# canvas
frame = Frame(root, width=500, height=500)
frame.pack()

def popup(event):
    menu.post(event.x_root, event.y_root)

frame.bind("<Button-3>", popup)
#root.config(menu=menu)
root.mainloop()