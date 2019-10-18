class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def whoAmI(self):
        return 'I am a Person, my name is %s' % self.name


class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

    def whoAmI(self):
        return 'I am a Student, my name is %s' % self.name


class Teacher(Person):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course

    def whoAmI(self):
        return 'I am a Teacher, my name is %s' % self.name


def who_am_i(x):
    print(x.whoAmI())


p = Person('Tim', 'Male')
s = Student('Bob', 'Male', 88)
t = Teacher('Alice', 'Female', 'English')

who_am_i(p)
who_am_i(s)
who_am_i(t)

'''
practice
Python提供了open()函数来打开一个磁盘文件，并返回 File 对象。File对象有一个read()方法可以读取文件内容：
例如，从文件读取内容并解析为JSON结果：
import json
f = open('/path/to/file.json', 'r')
print json.load(f)

由于Python的动态特性，json.load()并不一定要从一个File对象读取内容。任何对象，只要有read()方法，就称为File-like Object，都可以传给json.load()。
请尝试编写一个File-like Object，把一个字符串 r'["Tim", "Bob", "Alice"]'包装成 File-like Object 并由 json.load() 解析。
'''

import json


class Students(object):

    def read(self):
        return r'["Tim", "Bob", "Alice"]'


s = Students()

print(json.load(s))
