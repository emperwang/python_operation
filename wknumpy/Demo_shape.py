# coding:utf-8
import numpy as np

# shape 和 reshape的使用

a = np.array([1, 2, 3, 4, 5])
# 查看数组的带下
print(a.shape)

b = np.array([[1, 2, 3], [4, 5]])
print(b.shape)

# 调用reshape改变数组的维度, 并重新排列, 同时, 保存数组的大小不变
c = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(c.shape)
# 第一个参数标识几维  第二个参数为  每一个维的数量
d = c.reshape(2, 5)
print(d)
print(d.shape)

# 由此可见, 第二个标识有效, 则整体就有效
e = c.reshape(-1, 2)
print(e)
print(e.shape)