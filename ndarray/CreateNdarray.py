# Author:panta
# CreateDate:2019/11/6
# FileName:0003
# IDE:PyCharm

import numpy as np


# 创建空数组，值为随机值
a = np.empty((2,3),dtype=int)
print(a)

b = np.zeros((2,3), order = 'F')
print(b)

# 默认为浮点数
c = np.zeros((3,3))
print(c)
d = np.zeros((3,4), dtype=np.int)
print(d)

e = np.zeros((2,3),dtype=[('x','i4'),('y','i4')])
print(e)