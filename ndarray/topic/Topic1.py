# Author:panta
# CreateDate:2019/11/14
# FileName:Topic1
# IDE:PyCharm


import numpy as np
import numpy.matlib as mb

def check1(x):
    if x is None:
        return False
    right = np.zeros(len(x))
    return np.array_equal(x, right)


def check2(x):
    if x is None:
        return False
    right = np.zeros(len(x))
    right[4] = 1
    return np.array_equal(x, right)


def check3(x):
    if x is None:
        return False
    right = np.arange(10, 50)
    return np.array_equal(x, right)


def check4(x):
    if x is None:
        return False
    right = np.arange(9).reshape(3, 3)
    return np.array_equal(x, right)

def check5(result,test_case):
    if result is None or test_case is None:
        return False
    a = np.nonzero(test_case)
    return np.array_equal(result, a)

def check6(result):
    if result is None:
        return False
    a = mb.identity(len(result))
    return (result == a).all()


# 创建一个 长度为10，每个值都为0的向量 （或长度为任意）， 重点是 零向量、0向量的生成

zero = np.zeros(10)

assert check1(zero), "0 向量生成出错"
assert isinstance(zero, np.ndarray), "转换 np.array 失败"

zero[4] = 1
assert check2(zero), "0 向量生成出错"

# 创建从 10到49的向量， 重点是区间范围， 如 range()
range = np.arange(10, 50)
assert check3(range), "生成某区间向量出错"

# 创建3x3矩阵， 值从0到8。 重点是array的变形， 数组、矩阵的size变换
reshape = np.arange(0, 9).reshape(3, 3)
assert check4(reshape), "某区间向量转换成指定行列矩阵出错"

# 查找 [1,2,0,0,4,0] 里的非零元素，并返回下标。
p = np.array([1, 2, 0, 0, 4, 0])
result = np.nonzero(p)
assert check5(result, p), "向量非0元素索引出错"

# 创建一个3x3的单位矩阵
unit_matrix =  mb.identity(3)
assert  check6(unit_matrix),"生成单位矩阵出错"

#  创建一个3x3x3的随机数组
z = np.random.random((3,3,3))
print(z)

# 创建一个10x10的随机数组，并找出该数组中的最大值与最小值
a = np.random.random((10,10))
print(a)
print(np.amax(a),a.max())
print(np.amin(a),a.min())

#  创建一个长度为30的随机向量，并求它的平均值
a = np.random.random(30)
print(np.average(a),np.mean(a))

# 创建一个2维数组，该数组边界值为1，内部的值为0
b = np.ones((10,10))
b[1:-1,1:-1] = 0
print(b)

# 如何用0来填充一个数组的边界？
print(np.pad(b, pad_width=1, mode='constant', constant_values=0))

c = np.nan * 0
print(c)
print(np.nan == np.nan)
print(np.inf > np.nan)
print(np.nan - np.nan)
print(0.3 == 3 * 0.1)

