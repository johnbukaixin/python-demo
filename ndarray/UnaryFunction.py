# Author:panta
# CreateDate:2019/11/11
# FileName:UnaryFunction
# IDE:PyCharm

import numpy as np

a = np.arange(1,25).reshape((2,3,4))
print('a--->',a)

#元素平均值
c = a.mean()
print(c)

# # 计算a与元素平均值的商
b = a / c
print('计算a与元素平均值的商a / a.mean()-->','原数组',a,'新数组',b)

# 绝对值
abs1 = np.abs(b)
fabs1 = np.fabs(b)
print('abs原数组',b,'新数组',np.abs(b))
print('fabs原数组',b,'新数组',np.fabs(b))

# 各元素的平方根
print('各元素的平方根sqrt',a,np.sqrt(a))
# 各元素的平方数
print('各元素的平方数square',a,np.square(a))

print('log',a,np.log(a))
print('log10',a,np.log10(a))
print('log2',a,np.log2(a))
# 向上取整
print('向上取整ceil',np.ceil(a))
# 向下取整
print('向下取整floor',np.floor(a))
print('计算数组个元素的四舍五入值',np.rint(b))

print('将数组个元素的小数和整数部分以两个独立数组形式返回modf()',np.modf(b))

#np.cos(x) np.cosh(x)
#np.sin(x) np.sinh(x)
#np.tan(x) np.tanh(x)
cos = np.cos(b)

print('三角函数',b,cos)

print('计算数组个元素的指数值',a,np.exp(a))

print('计算数组各元素的符号值',a,np.sign(a))
