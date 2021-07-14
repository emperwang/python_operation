# coding:utf-8

import numpy as np

#  创建一维数组
a = np.array([1, 2, 3, 4, 5], dtype=np.int32)
print(a)
print(type(a))
print(a.dtype)

# 多维数组创建
b = np.array([[1, 2], [3, 4], [5, 6]], dtype=np.int)
print(b)

# 内置函数来创建数组 start end interval
c = np.arange(1, 10, 1)
print(c)
print(type(c))
print(c.dtype)


# linspace创建数组, 指定开始值, 终止值以及元素个数来创建一维数组, 该数组各个值成等差数列
d = np.linspace(1, 10, 30)
print(d)

# logspace 创建数组, 指定开始 终止值 以及元素个数来创建一维数组, 该数组各个值成等比数列
e = np.logspace(1, 10, 20)
print(e)

# fromfunction函数创建数组, 该函数的第一个参数为计算数据元素的函数,第二个参数是代表数组的大小的序列, 序列的每一个值代表对应维度的大小

def fun(a):
    return a+a

f = np.fromfunction(fun, (10, ))
print(f)

def funb(i, j):
    return i+j

g = np.fromfunction(funb, (3, 3))
print(g)