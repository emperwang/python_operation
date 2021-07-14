from tkinter import *

#root = Tk()

m = PanedWindow(orient=VERTICAL)
m.pack(fill=BOTH, expand=1)

top = Label(m, text="top pane")
m.add(top)

buttom = Label(m, text="bottom pane")
m.add(buttom)

mainloop()
#root.mainloop()