from tkinter import *
from tkinter import colorchooser

root = Tk()

# 属性:
# initialcolor:
# parent
# title

def choosecolor():
    color = colorchooser.askcolor(title="选择颜色")
    print("color={}".format(str(color)))

Button(root, text="选择颜色", command=choosecolor).pack()


root.mainloop()