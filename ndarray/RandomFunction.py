# Author:panta
# CreateDate:2019/11/11
# FileName:RandomFunction
# IDE:PyCharm

import numpy as np

# 创建随机数组，浮点数[0,1)均匀分布
np.random.rand(2,3)

# 标准正态分布
np.random.randn(2,3)
# 100~200d范围内获取值，生成数组
b = np.random.randint(100,200,(3,4))

# 设置相同seed值获得相同数组
np.random.seed(10)
np.random.randint(100,200,(3,4))
np.random.seed(10)
np.random.randint(100,200,(3,4))

a = np.random.randint(100,200,(3,4))
print(a)

np.random.shuffle(a)
print(a)

np.random.shuffle(a)
print(a)

c = np.random.randint(100,200,(3,4))
print(c)
np.random.permutation(c)

print(c)
