# coding:utf-8

import numpy as np

# 创建一个数组
a = np.array([1, 2, 3, 4, 5])
print(a.dtype)

# to file  以二进制方式写入文件
a.tofile('b.bin')

# fromfile  从文件中加载; 以二进制形式加载
b = np.fromfile('b.bin', dtype=np.int32)
print(b)

# save  以numpy专有格式存取
np.save('a.npy', a)

# load 以numpy专有格式存取
c = np.load('a.npy')

# savez 可以保存多个数组到同一个文件
a1 = np.array([[1, 2, 3], [4, 5, 6]])
a2 = np.array([3, 2, 1])
a3 = np.arange(10, 15, 2)
np.savez('data.npz', a1, a2, a3)
#load
arr = np.load('data.npz')
# 使用load读取数据  并把每行 打印出来
print(arr['arr_0'])
print(arr['arr_1'])
print(arr['arr_2'])
