# Author:panta
# CreateDate:2019/11/11
# FileName:IndexSplice
# IDE:PyCharm

import numpy as np

a = np.array([9,8,7,6,5])
print(a[1])
# 起始编号: 终止编号(不含): 步长，3元素冒号分割
print('a[1:4:2]--->',a[1:4:2])

b = np.arange(24).reshape((2,3,4))
print('b---->',b)
# 每一个维度一个索引值，逗号分割
print('b[1,2,3] --->',b[1,2,3])
print('b[0,1,2]--->',b[0,1,2])
print('b[-1,-2,-3]--->',b[-1,-2,-3])

c = np.arange(24).reshape((2,3,4))
print('c---->',c)
# 选取一个维度用
print('c[:,1,-3]--->',c[:,1,-3])
#每个维度切片方法与一维数组相同
print('c[:,1:3,:]-->',c[:,1:3,:])
#每个维度可以使用步长跳跃切片
print('c[:,:,::2]-->\n',c[:,:,::2])