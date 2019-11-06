# Author:panta
# CreateDate:2019/11/6
# FileName:0002
# IDE:PyCharm

import numpy as np

# 现在是两行三列
b = np.array([[1, 2, 3], [3, 4, 5]], dtype='i4')
print(b)
# b 现在变成了三行两列
b.shape = (3, 2)
print(b)
print(b.ndim)
print(b.shape)
print(b.size)
print(b.dtype)
print(b.data)

# 生成一个一维数组 [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
a = np.arange(24)
print(a)
print(a.ndim)

c = a.reshape(2, 4, 3)  # b 现在拥有三个维度
print(c)


x = np.array([1,2,3,4,5],dtype=np.int8)

print(x.itemsize)

y = np.array([1,2,3,4,5],dtype=np.float)
print(y.itemsize)

z = np.array([1,2,3,4,5])
print (z.flags)