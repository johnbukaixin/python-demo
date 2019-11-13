# Author:panta
# CreateDate:2019/11/13
# FileName:SeniorIndex
# IDE:PyCharm
import numpy as np

x = np.array([[1, 2], [3, 4], [5, 6]])

y = x[[0, 1, 2], [0, 1, 0]]
print(y)

z = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

print(z)

w = z[[1, 0, 1, 0], [1, 1, 1, 1]]
print(w)

a = np.arange(9).reshape((3, 3))
print(a)

print(a[a > 5])

a = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
print(a[~np.isnan(a)])

b = np.array([1, 2 + 6j, 5, 3.3 + 5j])
print(b[np.iscomplex(b)])

a = np.array([1, 2 + 6j, 5, 3.5 + 5j])
print(a[np.iscomplex(a)])

c = np.arange(32).reshape(8, 4)
print(c)

print(c[[4, 2, 1, 7]])

