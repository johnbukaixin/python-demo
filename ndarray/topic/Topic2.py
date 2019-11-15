# Author:panta
# CreateDate:2019/11/15
# FileName:Topic2
# IDE:PyCharm


import numpy as np

# 创建一个numpy数组元素值全为True（真）的数组
a = np.full((3, 3), True, dtype=np.bool)
print(a)

# 如何从一维数组中提取满足指定条件的元素？ 从 arr 中提取所有的奇数
b = np.arange(12)
condition = b % 2 == 1
c = np.extract(condition, b)
d = b[b % 2 == 1]
print(c)
print(d)

# 如何用numpy数组中的另一个值替换满足条件的元素项？
b[b % 2 == 1] = -1
print(b)

# 如何在不影响原始数组的情况下替换满足条件的元素项？
new_array = np.where(b % 2 == 1, -1, b)
print(new_array)
copy = b.copy()
copy[copy % 2 == 1] = -1
print(copy)

# 如何改变数组的形状？
reshape = np.arange(10).reshape(2, 5)
print(reshape)

# 如何垂直叠加两个数组？
overlay1 = np.arange(12).reshape(3, 4)
overlay2 = np.copy(overlay1)
vertical_concatenate = np.concatenate([overlay1, overlay2], axis=0)
print(vertical_concatenate)
# 如何水平叠加两个数组？
overlay3 = np.arange(9).reshape(3, 3)
level_concatenate = np.concatenate([overlay1, overlay3], axis=1)
print(level_concatenate)

# 如何在无硬编码的情况下生成numpy中的自定义序列？
a = np.array([1, 2, 3])
repeat = np.repeat(a, 3)
tile = np.tile(a, 3)
init_ser = np.concatenate([repeat, tile])
print(init_ser)
print(np.r_[np.repeat(a, 3), np.tile(a, 3)])

# 如何获取两个numpy数组之间的公共项？
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
print(np.intersect1d(a, b))

# 如何从一个数组中删除存在于另一个数组中的项？
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 6, 7, 8, 9])
# From 'a' remove all of 'b'
print(np.setdiff1d(a, b))

# 如何得到两个数组元素匹配的位置？
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
print(np.where(a == b))

# 如何从numpy数组中提取给定范围内的所有数字？
a = np.array([2, 6, 1, 9, 10, 3, 27])
b = np.arange(5, 11)
print(np.intersect1d(a, b))
index = np.where(np.logical_and(a >= 5, a <= 10))
print(a[index])

print(type(a))
