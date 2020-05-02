from tkinter import *
from tkinter import filedialog

root = Tk()

def calback():
    fileName = filedialog.askopenfilename(filetypes=[("PNG", ".png"), ("GPF", ".gpf"), \
                                                     ("JPG", "jpg"), ("TEXT", ".txt")])
    print("filename={}".format(fileName))


Button(root, text="Openfile", command=calback).pack()

# 属性:
# defaultextension  默认添加的文件尾缀
# filetypes 文件类型，以元组(tuple)形式定义
# initialdir 初始化目录
# initialfile   初始化文件
# parent   父级容器
# title     

# 选择打开什么文件,返回文件名
# filedialog.askopenfilename()

# 选择打开什么文件, 返回io流对象
# filedialog.askopenfile()

# 选择目录, 返回目录名
# filedialog.askdirectory()

# 选择打开多个文件, 以元组形式返回多个文件名
# filedialog.askopenfilenames()

# 选择打开多个文件,以列表形式返回多个io流对象
# filedialog.askopenfiles()

# 选择以什么文件保存, 创建文件并返回文件流对象
# filedialog.asksaveasfile()

# 选择以什么文件名保存, 返回文件名
# filedialog.asksaveasfilename()


root.mainloop()