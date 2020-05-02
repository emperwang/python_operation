#!/bin/env python
# coding:utf-8
# py3

from tkinter import *
from tkinter import messagebox

# 根面板
root = Tk()

root.title("first GUI")
root.geometry("500x400+100+200")

# 创建一个button 并放置在root中
btn1 = Button(root)
btn1['text'] = "click me"

btn1.pack()

def songhua(e):
    messagebox.showinfo("message", "送你小花花")

# 事件绑定
btn1.bind('<Button-1>', songhua)

root.mainloop()
