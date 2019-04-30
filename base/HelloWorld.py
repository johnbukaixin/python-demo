print("Hello, Python!")

student = {'Tom', 'Jack', 'Rose', 'Jerry', 'Tom'}
print(student)
if 'Tom' in student:
    print('Tom is in student')
else:
    print("Tom 不在集合中")

# 进行集合计算,集合元素自动去重
a = set('ddddc')  # set函数声明集合
b = set('cccc')

print(a - b)
print(a)
print(a | b)
print(a & b)
print(a ^ b)

dict = {'one': 1, 2: 2}
tinyDict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
dict.copy()
print(dict)
print(dict['one'])
print(dict[2])
print(tinyDict)
print(tinyDict.keys())
print(tinyDict.values())
# 构造函数 dict() 可以直接从键值对序列中构建字典如下：
# dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
# {x: x ** 2 for x in (2, 4, 6)}
# dict(Runoob=1, Google=2, Taobao=3)

"""
int(x [,base])

将x转换为一个整数

float(x)

将x转换到一个浮点数

complex(real [,imag])

创建一个复数

str(x)

将对象 x 转换为字符串

repr(x)

将对象 x 转换为表达式字符串

eval(str)

用来计算在字符串中的有效Python表达式,并返回一个对象

tuple(s)

将序列 s 转换为一个元组

list(s)

将序列 s 转换为一个列表

set(s)

转换为可变集合

dict(d)

创建一个字典。d 必须是一个序列 (key,value)元组。

frozenset(s)

转换为不可变集合

chr(x)

将一个整数转换为一个字符

ord(x)

将一个字符转换为它的整数值

hex(x)

将一个整数转换为一个十六进制字符串

oct(x)

将一个整数转换为一个八进制字符串
"""

