from tkinter import *

root = Tk()

w = Canvas(master=root)
w.pack()

# 画一条线
w.create_line(500, 500, 200, 100, fill="black")
# 画一个矩形
w.create_rectangle(0, 100, 200, 0, fill="red", dash=(4, 4))
#w.create_arc(0, 100, 200, 0, fill="yellow")

# 画椭圆
w.create_oval(0, 100, 200, 0, fill="yellow")

root.mainloop()