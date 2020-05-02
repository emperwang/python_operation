from tkinter import *

root = Tk()
root.title("entry")
root.geometry("500x400+200+200")
strval = StringVar()
pwd = StringVar()

def printVal():
    print(strval.get())

def validatepassword():
    print("validaing password.")
    pd = password.get()
    print("pd = {}".format(pd))

e = Entry(root, textvariable=strval)
e.pack(side=TOP)
e.delete(0, END)
# e.insert(0, "Default value")
strval.set("Initial val")


# password entry
password = Entry(root, text="password", show="*", validate="focusout", vcmd=validatepassword)
password.pack()


Button(root, text="printVal", fg="blue", bg="black", command=printVal).pack()


root.mainloop()