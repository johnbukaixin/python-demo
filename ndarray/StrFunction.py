# Author:panta
# CreateDate:2019/11/14
# FileName:StrFunction
# IDE:PyCharm
import numpy as np

print(np.char.add('a','b'))
print(np.char.add(['a'],['b']))

print(np.char.add(['a','b'],['c','d']))


print(np.char.multiply('hello',3))

# str: 字符串，width: 长度，fillchar: 填充字符
print(np.char.center('hello',20,fillchar='*'))

print(np.char.capitalize('hello'))


print(np.char.title('i like runoob'))

print(np.char.lower(['HELLO','WORLD']))


print(np.char.splitlines('i\nlike runoob?'))
print(np.char.splitlines('i\rlike runoob?'))