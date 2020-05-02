#!/bin/env python
# coding:utf-8

from tkinter import *
from tkinter import messagebox


class application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        self.btn1 = Button(self, text="送花", command=self.songhua)
        self.btn1.pack()
        self.btnQuit = Button(self, text="quit", command=root.destroy)
        self.btnQuit.pack()

    def songhua(self):
        messagebox.showinfo("message", "送你小花花")


if __name__ == '__main__':
    root = Tk()
    root.title("demo2")
    root.geometry("500x400+200+200")
    app = application(master=root)
    root.mainloop()
