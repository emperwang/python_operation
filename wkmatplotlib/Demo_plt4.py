# coding:utf-8

import matplotlib.pyplot as plt
from matplotlib import font_manager

y = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
x = range(10, 30)

# 设置图形大小
# figsize 设置大小  dpi设置清晰度
plt.figure(figsize=(20, 8), dpi=80)

plt.plot(x, y)

# 设置刻度
_xticks = x
plt.xticks(_xticks)
plt.yticks(y)

# 显示
plt.show()