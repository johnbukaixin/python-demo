# Author:panta
# CreateDate:2019/11/14
# FileName:a
# IDE:PyCharm
import numpy as np

a = np.arange(9).reshape(3,3)

b = np.array([10,10,10])

np.add(a , b)

np.subtract(a,b)

np.divide(a,b)

np.multiply(a,b)

c = np.array([0.25,1.33,1,100])
np.reciprocal(c)

d = np.array([10,100,1000])

np.power(d,2)

np.power(d,[1,2,3])


e = np.array([10,20,30])

np.mod(e,3)

np.mod(e,[3,5,7])
np.remainder(e,3)
np.remainder(e,[3,5,7])
