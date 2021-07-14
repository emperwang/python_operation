# coding:utf-8

import matplotlib.pyplot as plt
from matplotlib import font_manager


y = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
y2 = [1, 0, 4, 5, 4, 4, 7, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
x = range(10, 30)


# 设置一个中文字体
# 后面的ttc是系统中使用的字体
myFont = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")

# 设置图形大小
# figsize 设置大小  dpi设置清晰度
plt.figure(figsize=(20, 8), dpi=80)

# plot的其他参数, color 设置线条颜色
# linestyle 设置线条风格
# linewidth 设置线条粗细
# alpha 设置透明度
plt.plot(x, y, label="自己")
plt.plot(x, y2, label="同桌")

# 设置label
plt.xlabel("年龄", fontproperties=myFont)
plt.ylabel("数量", fontproperties=myFont)
plt.title(" 不同年龄的女朋友数量", fontproperties=myFont)

# 设置刻度
_xticks = ["{} 岁".format(i) for i in x]

# rotation 旋转的度数
plt.xticks(x, _xticks, rotation=45, fontproperties=myFont)
plt.yticks(y)


# 显示网格, alpha 设置透明度
plt.grid(alpha=0.4)

# prop 设置字体
# loc 参数可以设置 图例的位置
plt.legend(prop=myFont)


# 保存图片
# plt.savefig("path..")

# 显示
plt.show()