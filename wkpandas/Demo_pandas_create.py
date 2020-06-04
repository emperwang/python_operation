# coding:utf-8

import pandas as pd
import numpy as np

# ------------------- 创建series对象 -------------------
# 传入list常见series,并生成默认的整形索引
s1 = pd.Series([1, 2, 3, 4, 5])
print(s1)
## 指定 index
s2 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(s2)

# 传入numpy的ndarray数组创建
s3 = pd.Series(np.arange(1, 5, 1))
print(s3)

# ------------------ 创建DataFrame对象 ------------------
d1 = pd.date_range('20170501', periods=5)
print(d1)

d2 = pd.DataFrame(np.random.randn(5, 4), index=d1, columns=list("ABCD"))
print(d2)

# 传入 dict来创建dataFrame
d3 = pd.DataFrame({"a":1, "b":2, "c":3, "d":4, "e":("e1", "e2", "e3")})
print(d3)
