from tkinter import *
from tkinter import messagebox


def showInfo(info):
    messagebox.showinfo("into", info)


def showWarn(info):
    messagebox.showwarning("warn", info)


def showError(info):
    messagebox.showerror("error", info)


def askOkOrCancel():
    rr = messagebox.askokcancel("okCancel", "继续还是取消?")
    print(rr)


def askQuestion():
    res = messagebox.askquestion("question", "please answer question.")
    print("answer : {}".format(res))


def askYesOrNo():
    res = messagebox.askyesno("YN", "please select yes or no.")
    print("Yes Or No:{}".format(res))


def askIfRetry():
    rr = messagebox.askretrycancel("retry", "Are we retry it?")
    print("retry:{}".format(rr))


def askYesNoCancel():
    ret = messagebox.askyesnocancel("YNC", "Are we going to do it ?")
    print("yes no cancel:{}".format(ret))


root = Tk()
root.title("mesagebox")
root.geometry("400x500+200+200")

toolbar = Frame(root)
Button(toolbar, text="showinfo", width=6, command= lambda : showInfo("show info"))\
    .pack(side=LEFT, padx=2, pady=2)
Button(toolbar, text="showarn", width=6, command=lambda :showWarn("show warning"))\
    .pack(side=LEFT, padx=2, pady=2)
Button(toolbar, text="showerr", width=6, command=lambda: showError("show error"))\
    .pack(side=LEFT, padx=2, pady=2)
Button(toolbar, text="askOkOrCancel", command=askOkOrCancel)\
    .pack(side=LEFT, padx=2, pady=2)
Button(toolbar, text="askQuestion", command=askQuestion)\
    .pack(side=LEFT, padx=2, pady=2)
Button(toolbar, text="askYesOrNo", command=askYesOrNo)\
    .pack(side=LEFT, padx=2, pady=2)
Button(toolbar, text="askIfRetry", command=askIfRetry)\
    .pack(side=LEFT, padx=2, pady=2)
Button(toolbar, text="askYesNoCancel", command=askYesNoCancel)\
    .pack(side=LEFT, padx=2, pady=2)


toolbar.pack(side=TOP)

root.mainloop()