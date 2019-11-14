# Author:panta
# CreateDate:2019/11/14
# FileName:SortConditionFunction
# IDE:PyCharm
import numpy as np

a = np.random.randint(1, 11, (3, 4))

print(a)

np.sort(a, 0)

np.sort(a, 1)
a
np.argmax(a)
np.argmax(a, 0)
np.argmax(a, 1)
a.flatten()
a.flatten()[np.argmax(a)]

dt = np.dtype([('name', 'S10'), ('age', int)])

b = np.array([("raju", 21), ("anil", 25), ("ravi", 17), ("amar", 27)], dtype=dt)

np.sort(b, order='name')

c = np.array([2, 3, 1])

np.argsort(c)

c[np.argsort(c)]

for i in np.argsort(c):
    print(c[i], end=" ")

nm = ('raju', 'anil', 'ravi', 'amar')
dv = ('f.y.', 's.y.', 's.y.', 'f.y.')
ind = np.lexsort((dv, nm))
print('调用 lexsort() 函数：')
print(ind)
print('\n')
print('使用这个索引来获取排序后的数据：')
print([nm[i] + ", " + dv[i] for i in ind])

d = np.random.randint(10, size=(3, 4))

print(d)

np.nonzero(d)

x = np.where(d > 3)

print(d[x])

print(d)
condition = np.mod(d, 2) == 0

print(np.mod(d, 2))
print(condition)
print(np.extract(condition, d))
