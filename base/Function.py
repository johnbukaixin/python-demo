import math


def hello():
    print("hello world")


hello()


def area(length, width):
    return length * width


print(area(10, 2))


def printName(name):
    print("hello world,", name)


printName("zhangsan")


# 参数传递 类型属于对象，变量是没有类型的： 可变参数和不可变参数

def changeInt(b):
    b = 10


b = 2
changeInt(b)
print(b)


def changeList(lis):
    if len(lis) > 0:
        lis[0] = 21


listVar = [1, 32, 3, 4, 50]
changeList(listVar)

print(listVar)


#  参数
# 必须参数、关键字参数、默认参数、不定长参数
#  必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。
# 关键字参数 可以通过参数名匹配参数
# 关键字参数
# 关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
#
# 使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。
#
# 以下实例在函数 printme() 调用时使用参数名：
def printStr(str):
    print(str)
    return


# 不传参数会报错
# printStr()

printStr(str='s')


# 定义函数设置默认值
def printPerson(age, name='李四'):
    print("your name,", name)
    print('your age,', age)


printPerson(name='张三', age=12)
printPerson(age=12)

'''
def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
   
'''


# 不定长参数 星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
# 如果在函数调用时没有指定参数，它就是一个空元组。


def printInfo(arg1, *tupleArgs):
    print(arg1)
    print(tupleArgs)


printInfo(2, 3, 4, 5)

'''
   def functionname([formal_args,] **var_args_dict ):
   "函数_文档字符串"
   function_suite
   return [expression]
'''

# 不定长参数 星号 ** 的参数会以字典(dict)的形式导入。

# 匿名函数 使用lambda来创建匿名函数

sum = lambda arg1, arg2: arg1 + arg2

print(sum(2, 4))

# 变量作用域
# Python的作用域一共有4种，分别是：
#
# L （Local） 局部作用域
# E （Enclosing） 闭包函数外的函数中
# G （Global） 全局作用域
# B （Built-in） 内置作用域（内置函数所在模块的范围）
# 内置作用域是通过一个名为 builtin 的标准模块来实现的
# >>> import builtins
# >>> dir(builtins)

gCount = 0  # 全局作用域


def outer(a):
    oCount = 1  # 闭包函数外作用

    def inner():
        iCount = 2  # 局部作用域
        print("作用域测试", a)
        return a

    return inner()


outer(1)

# 模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
# 其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问

#  可以访问
# >>> if True:
# ...  msg = 'I am from Runoob'
# ...
# >>> msg
# 'I am from Runoob'
# >>>

#  访问出错
# >>> def test():
# ...     msg_inner = 'I am from Runoob'
# ...
# >>> msg_inner
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'msg_inner' is not defined
# >>>

numbers = [1, 3, 6]
newNumbers = tuple(map(lambda x: x, numbers))
print(newNumbers)


def printa(s1, s2):
    return s1, s2


r = printa("a", "v")

print(r)


def quadratic_equation(a, b, c):
    t = math.sqrt((b * b - 4 * a * c))
    x1 = (-b + t) / (2 * a)
    x2 = (-b - t) / (2 * a)
    return x1, x2


print(quadratic_equation(2, 3, 0))
print(quadratic_equation(1, -6, 5))


def average(*args):
    avg = 0
    sum = 0
    for num in args:
        sum = sum + num
        avg = sum / len(args)
    return avg


print(average())
print(average(1, 2))
print(average(1, 2, 2, 3, 4))


def firstCharUpper(s):
    return s[:1].upper() + s[1:]


print(firstCharUpper('hello'))
print(firstCharUpper('sunday'))
print(firstCharUpper('september'))


# 定义一个函数，有三个参数，前两个参数为数值，最后一个参数为函数，计算传入abs函数的值

def add(x, y, f):
    return f(x) + f(y)


print(add(2, 3, abs))
import math


def add(x, y, f):
    return f(x) + f(y)


print(add(25, 9, math.sqrt))


def format_name(s):
    L = []
    for str1 in s:
        newStr = str1[:1].upper() + str1[1:]
        L.append(newStr)
    return L


map(format_name, ['adam', 'LISA', 'barT'])


def is_sqr(x):
    num = math.sqrt(x)
    if isinstance(num, int):
        return num


print(filter(is_sqr, range(0, 101)))

import math


def is_sqr(x):
    print(math.sqrt(x))
    return math.sqrt(x) % 1 == 0


print(filter(is_sqr, range(1, 101)))

print(9.0 % 1 == 0)


def count():
    fs = []
    for i in range(1, 4):
        def f(j=i):
            return j * j

        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())

f4,f5,f6 = [1,2,3]

print(f4,f5,f6)
print (sorted([1, 3, 9, 5, 0],reverse=True))

import operator

print(operator.le(1,3))
print(operator.le(1,1))
print(operator.lt(1,4))
print(operator.ge(3,4))
print(operator.ge(3,3))
print(operator.gt(4,3))
print(operator.gt(3,4))
print('{0}和{site}'.format('谷歌',site='www.google.com'))



