# coding:utf-8

import matplotlib.pyplot as plot
import numpy as np

# 0到5之间 每隔0.2 取一个数
t = np.arange(0, 5, 0.2)

# 红色破折号  蓝色方块  绿色三角形
plot.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plot.show()