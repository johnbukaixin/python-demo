#  算数运算符
a = 10
b = 20
c = 0

c = a + b
print("1 - c的值", c)
c = a - b
print("2 - c 的值", c)
c = a | b
print("3 - c的值", c)
c = a * b
print("4 - c 的值", c)
c = a / b
print("5 - c 的值", c)
c = a % b
print("6 - c 的值", c)
a = 2
b = 3
c = a ** b
print("6 - c 的值", c)
a = 10
b = 5
c = a // b
print("7 - c 的值为：", c)

#  is 与 == 区别：
d = [1, 2, 3, 4, 5]
e = d
print(e == d)
print(e is d)
#  id() 函数用于获取对象内存地址。
print(id(e) == id(d))
e = d[:]
print(e)
print(e == d)
print(e is d)

# and	x and y	布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	(a and b) 返回 20。
# or	x or y	布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。	(a or b) 返回 10。
# not	not x	布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not(a and b) 返回 False
# 优先级 not > and > or 在没有括号的前提下

