# coding:utf-8
import numpy as np

# 数学函数
# 数学函数包含add subtract, multiply divide  log sqrt等一系列函数

a = np.arange(1, 6, 1)
b = np.arange(6, 11, 1)
print(a)
print(b)
# 数组相加
print("-----add-------")
print(a+b)
print(np.add(a, b))
print("-----sub-------")
print(b-a)
print(np.subtract(b, a))
print("-----mul-------")
print(a * b)
print(np.multiply(a, b))
print("-----div-------")
print(b / a)
print(np.divide(b, a))
print("-----log-------")
print(np.log(a))

print("-----sqrt------")
print(np.sqrt(a))


# 三角函数
# 包含isn, cos,tan等一些函数,需要说明的是 其参数并不是直接代表三角函数的度数, 而是使用pi代替,2pi相当于360度
print("---------三角函数----------")
print(np.sin(np.pi/2))
a = np.sin(np.array((0, 30, 45, 60, 90)) * np.pi/180)
print(a)

# 位操作函数
# 包含 按位的与  或  异或  左移  右移操作
print(np.binary_repr(5))
print(np.binary_repr(7))

# 与
print(np.bitwise_and(5, 7))
# 或
print(np.bitwise_or(5, 7))
# 异或
print(np.bitwise_xor(5, 7))
# 右移
print(np.right_shift(5, 2))
# 左移
print(np.left_shift(5, 2))

# 比较函数
print(np.greater([1, 5], [2, 10]))
print(np.equal([2, 10], [2, 14]))
print(np.greater_equal([1, 5], [1, 6]))
x = np.arange(1, 5)
print(np.logical_and(x > 1, x < 4))

# 浮点函数
# 包含了 类型判别, 是否是最大值, 向上取整等操作
print(np.iscomplex([3+1j, 6+0j, 7.5, 5, 2j]))

print(np.isinf(np.inf))

a = np.array([2.1, -2.1, 3.54, 7, 2, -7.2])
# 向上取整
print(np.ceil(a))
# 向下取整
print(np.floor(a))