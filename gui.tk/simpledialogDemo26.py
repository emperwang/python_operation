from tkinter import *
from tkinter import simpledialog

root = Tk()


#属性:
# initialvalue
# parent
# minvalue
# maxvalue

def askFloat():
    ret = simpledialog.askfloat("float", "Please input a float value")
    print("float={}".format(ret))

def askInt():
    ret = simpledialog.askinteger("int", "please input int value.")
    print("int = {}".format(ret))

def askStr():
    ret = simpledialog.askstring("string", "Please input a string.")
    print("string={}".format(ret))


Button(root, text="float", command=askFloat).pack()
Button(root, text="int", command=askInt).pack()
Button(root, text="string", command=askStr).pack()

root.mainloop()