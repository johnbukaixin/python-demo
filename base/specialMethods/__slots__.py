# Author:panta
# CreateDate:2019/10/30
# FileName:Slot
# IDE:PyCharm
class Person(object):

    __slots__ = ('name', 'gender')

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):

    __slots__ = ('name','gender','score')

    def __init__(self, name, gender, score):
        super().__init__(name, gender)
        self.score = score

s = Student('Bob', 'male', 59)
s.name = 'Tim'
s.score = 99
print(s.score)
