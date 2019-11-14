# Author:panta
# CreateDate:2019/11/14
# FileName:Nditer
# IDE:PyCharm

import numpy as np

a = np.arange(6).reshape(2, 3)

for x in np.nditer(a):
    print(x)

b = np.arange(6).reshape(2, 3)
b.T
for x in np.nditer(b.T):
    print(x)

for x in np.nditer(b.T.copy(order='C')):
    print(x)

c = np.arange(0, 60, 5).reshape(3, 4)

print(c)

print(c.T)

for x in np.nditer(c):
    print(x)

for x in np.nditer(c, order='C'):
    print(x)

for x in np.nditer(c, order='F'):
    print(x)