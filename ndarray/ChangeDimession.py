# Author:panta
# CreateDate:2019/11/14
# FileName:ChangeDimession
# IDE:PyCharm

import numpy as np

ones = np.ones((2, 3, 4), dtype=np.int32)

print('ones----->', ones)

# 不改变原数组，返回一个shape形状的数组，原数组不变
reshape1 = ones.reshape((3, 8))
print('reshape1--->', reshape1)

# 与reshape函数功能一致，但修改原数组
resize2 = ones.resize((3, 8))
print('resize2----->', resize2)
print('resize2----->', ones)

b_ones = np.ones((2, 3, 4), dtype=np.int32)
print('b_ones--->', b_ones)

# 对数组进行降维，返回折叠后的一维数组，原数组不变
b_ones.flatten()
print('b_ones', b_ones)

c = b_ones.flatten()
c
print('c---->', c)

d = np.arange(12).reshape(3, 4)

print(d)

np.transpose(d)

a = np.array([[1, 2], [3, 4], [5, 6]])

print('第一个数组：')
print(a)
print('\n')

print('未传递 Axis 参数。 在插入之前输入数组会被展开。')
print(np.insert(a, 3, [11, 12]))
print('\n')
print('传递了 Axis 参数。 会广播值数组来配输入数组。')

print('沿轴 0 广播：')
print(np.insert(a, 1, [11], axis=0))
print('\n')

print('沿轴 1 广播：')
print(np.insert(a, 1, 11, axis=1))

a = np.arange(12).reshape(3, 4)

print('第一个数组：')
print(a)
print('\n')

print('未传递 Axis 参数。 在插入之前输入数组会被展开。')
print(np.delete(a, 5))
print('\n')

print('删除第二列：')
print(np.delete(a, 1, axis=1))
print('\n')

print('包含从数组中删除的替代值的切片：')
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(np.delete(a, np.s_[::2]))