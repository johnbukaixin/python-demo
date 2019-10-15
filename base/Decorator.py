# 1.定义一个函数，在不修改函数代码的前提下，对函数的功能进行拓展。比如权限验证。
def f1():
    print("这里f1函数的功能展示")


# 2.定义一个高级函数（闭包）实现对f1()函数进行权限验证。
def fn(f1):
    def fc():
        print("这里开始对f1函数权限进行验证")
        f1()
        print("f1函数已经处理完毕了")

    return fc


# 3.实现：对函数调用，实现对f1()函数调用的权限验证。
t = fn(f1)
t()  # t()相当于fn(f1)().表示对fn(f1)里面的函数fc()调用

# 打印日志
import logging


def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warning("%s is running" % func.__name__)
            return func(*args)

        # logging.info("hahha")
        return wrapper

    return decorator


@use_logging(level="warn")
def foo(name='foo'):
    print("i am %s" % name)


foo()

view_registry = []


def register(func):
    view_registry.append(func)
    return func


@register
def view1():
    pass


@register
def view2():
    pass


def main():
    print(view_registry)


main()

import time
import functools


# 计算程序运行时间
def performance(f):
    def print_time(*args, **kw):
        t1 = time.time()
        r = f(*args, **kw)
        t2 = time.time()
        print('call %s() in %fs' % (f.__name__, (t2 - t1)))
        return r

    return print_time


@performance
def factorial(n):
    return functools.reduce(lambda x, y: x * y, range(1, n + 1))


print(factorial(10))


# 1.写出完整的装饰器(不用带参装饰器，就是普通装饰器)语法

def log(func):
    def wrapper():
        logging.warning("hello")
        return func()

    return wrapper


@log
def func():
    print("hhh")
    pass


func()


# 2.有一个计算两个数和的方法，为其添加一个确保两个参数都是int或float类型的装饰器，保证运算不会抛异常

def validate(func):
    def wrapper(*args, **kwargs):
        flag = False
        if len(args) != 2:
            logging.warning("参数数量不对")
            flag = True
            pass
        for val in args:
            if (not isinstance(val, int)) and (not isinstance(val, float)):
                logging.warning("参数类型不对")
                flag = True
                pass
        if not flag:
            return func(*args, **kwargs)

    return wrapper


@validate
def new_sum(x, y):
    return x + y


print(new_sum(1, 2))
print(new_sum(1, 's'))
print(new_sum(1))


# 3.有一个一次性录入人名并返回人名的方法(人名只考虑存英文)，为其添加一个装饰器，确保人名首字母大写


def de_capitalize(func):
    def wrapper(*args):
        s = args[0]
        new_str = s.capitalize()
        return func(new_str)

    return wrapper


@de_capitalize
def print_name(s):
    return s


print(print_name("gghhh"))

'''
拓展题：
 
1.原功能：entry_grade
*) 可以完成『成绩录入功能』
	-- 可以重复录入成绩，默认所有输入都是合法的(1~100之间的数)
	-- 当录入成绩为0时，结束成绩的录入
	-- 将录入的成绩保存在列表中并返回给外界，eg：[90, 80, 50, 70]
 
2.选择课程装饰器：choose_course
*) 为『成绩录入功能』新增选择课程的拓展功能，达到可以录入不同学科的成绩
	-- 可以重复输入要录制的学科名，然后就可以进入该门学科的『成绩录入功能』，录入结束后，可以进入下一门学科成绩录入
	-- 当输入学科名为q时，结束所有录入工作
	-- 将学科成绩保存在字典中并返回给外界，eg：{'math':[90, 80, 50, 70], 'english':[70, 50, 55, 90]}
 
3.处理成绩装饰器：deal_fail
*) 可以将所有录入的成绩按60分为分水岭，转换为 "通过" | "不通过" 进行存储
	-- 如果只对原功能装饰，结果还为list返回给外界，eg：["通过", "通过", "不通过", "通过"]
	-- 如果对已被选择课程装饰器装饰了的原功能再装饰，结果就为dict返回给外界，eg：{'math':["通过", "通过", "不通过", "通过"], 'english':["通过", "不通过", "不通过", "通过"]}

'''


# 判断输入的数是否位数字是否为数字
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def change_sign(v):
    new_sign = []
    if isinstance(v, list):
        for grade in v:
            if grade >= 60:
                new_sign.append('通过')
            else:
                new_sign.append('不通过')
        pass
    return new_sign

# 处理通过还是不通过
def deal_fail(func):
    def wrapper():
        value = func()
        if isinstance(value, dict):
            for k, v in value.items():
                new_sign = change_sign(v)
                value[k] = new_sign
            return value
        else:
            return change_sign(value)

    return wrapper
# 选择课程
def choose_course(func):
    def wrapper():
        course_dict = {}
        while True:
            str_course = input("请输入课程：")
            if str_course == 'q':
                logging.info("课程成绩录入结束")
                return course_dict
            if not str_course in course_dict:
                course_dict[str_course] = func()
                pass
            pass
        pass

    return wrapper

# 录入成绩
@choose_course
@deal_fail
def entry_grade():
    grades = []
    while True:
        str_grade = input("请输入成绩：")
        if is_number(str_grade):
            grade = int(str_grade)
            if grade in range(1, 101):
                grades.append(grade)

            if grade == 0:
                logging.info("成绩录入结束")
                return grades


print(entry_grade())




