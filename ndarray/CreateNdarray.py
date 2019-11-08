# Author:panta
# CreateDate:2019/11/6
# FileName:0003
# IDE:PyCharm

import numpy as np


#列表创建
x = np.array([1,2,3,4,5])
print('x===>',x)

#元组创建
y = np.array((2,3,4,5,6))
print('y===>',y)

# list和元组混合创建
z = np.array([[1,2],[3,4],(5,6)])
print('z===>',z)

arange = np.arange(10)
print('arange方法创建====>',arange)

# 根据shape生成一个全1数组
ones = np.ones((2,3,4,1))
print('ones----->',ones)

# 根据shape生成一个全0数组
zero = np.zeros((22, 256, 3))
print('zero----->',zero)

# 创建一个shape生成的数组，每个元素的值为value
full = np.full((2,3),2)
print('full-->',full)
# 创建一个正方的n*n的单位矩阵，对角线为1 其余为0
eye = np.eye(4)
print('eye--->',eye)

# 根据数组a的形状生成全1数组
one_like = np.ones_like(full)
print('one_like--->',one_like)

# 根据数组a的形状生成全0数组
zero_like = np.zeros_like(full)
print('zero_like--->',zero_like)

# 根据数组a的形状生成全value数组
full_like = np.full_like(z,3)
print('full_like--->',full_like)

linespace1 = np.linspace(2.0, 3.0, num=5)
print('linespace1----->',linespace1)

linespace2 = np.linspace(1, 10, 4)
print('linespace2----->',linespace2)

linespace3 = np.linspace(1, 10, 4,endpoint=False)
print('linespace3----->',linespace3)

concatenate = np.concatenate((x,y))
print('concatenate----->',concatenate)
