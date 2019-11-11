# Author:panta
# CreateDate:2019/11/6
# FileName:0001
# IDE:PyCharm

import numpy as np

# 创建数组
a = np.array([1, 2, 3])

print(a)

# 创建多维数组
b = np.array([[1, 2], [3, 4]])
print(b)

# 指定最小维度
c = np.array([1, 2, 3, 4], ndmin=3)
print(c)

# 指定数据类型
d = np.array([1, 2, 3, 4], dtype=complex)
print(d)

e = np.dtype(np.int32)
print(e)

dt = np.dtype('i4')
print(dt)

dt = np.dtype('<i4')
print(dt)

dt = np.dtype([('age', np.int32)])
print(dt)

# 首先创建结构化数据类型
dt = np.dtype([('age',np.int8)])
# 将数据类型应用于 ndarray 对象
a = np.array([(10,),(20,),(30,)], dtype = dt)
print(a)
# 类型字段名可以用于存取实际的 age 列
print(a['age'])

# 下面的示例定义一个结构化数据类型 student，包含字符串字段 name，整数字段 age，及浮点字段 marks，并将这个 dtype 应用到 ndarray 对象。
student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')])
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student)
print(a)


a = np.arange(6).reshape(2,3)
# 保存数据
np.savetxt('a.csv',a,fmt='%d',delimiter=',')
np.savetxt('1f.csv',a,fmt='%.1f',delimiter=',')

b = np.loadtxt('a.csv',delimiter=',')
print(b)
c = np.loadtxt('a.csv',dtype=np.int,delimiter=',')
print(c)

