# Author:panta
# CreateDate:2019/11/13
# FileName:Broadcast
# IDE:PyCharm
import numpy as np

d = np.array([[0, 0, 0],
              [10, 10, 10],
              [20, 20, 20],
              [30, 30, 30]])
e = np.array([[2, 2, 3],
              [1, 1, 1],
              [2, 2, 2],
              [3, 3, 3]])
d.shape
e.shape
print(e + d)

f = np.array([2, 2, 3])
print(d + f)

# 对两个数组，分别比较他们的每一个维度（若其中一个数组没有当前维度则忽略），满足：
# 数组拥有相同形状。
# 当前维度的值相等&&当前维度的值有一个是 1。

dt = np.dtype[('name','S10'),('age',int)]

b = np.array([("raju",21),("anil",25),("ravi",  17),  ("amar",27)], dtype = dt)

np.sort(b,order='name')

randinp.random.nt
