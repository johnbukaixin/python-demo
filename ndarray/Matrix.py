# Author:panta
# CreateDate:2019/11/14
# FileName:Matrix
# IDE:PyCharm

import numpy.matlib
import numpy as np

print(np.matlib.empty((2, 2)))
# 填充为随机数据

np.matlib.zeros((2, 2))

np.matlib.eye(3, 4)

np.matlib.identity(5)

np.matlib.rand((3, 3))

b = np.matrix([[1, 2], [3, 4]])

c = np.asarray(b)

d = np.asmatrix(c)
