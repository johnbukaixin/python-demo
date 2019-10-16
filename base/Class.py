import functools


class Person():
    def __init__(self):
        self.name = None

    pass


p1 = Person()
p1.name = 'Bart'

p2 = Person()
p2.name = 'Adam'

p3 = Person()
p3.name = 'Lisa'


def cmp(s1, s2):
    if s1.name > s2.name:
        return 1
    if s1.name < s2.name:
        return -1
    return 0


L1 = [p1, p2, p3]
L2 = sorted(L1, key=functools.cmp_to_key(cmp))

print(L2[0].name)
print(L2[1].name)
print(L2[2].name)


class Person(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count = Person.count + 1


p1 = Person('Bob')
print(Person.count)

p2 = Person('Alice')
print(Person.count)

p3 = Person('Tim')
print(Person.count)

class Person1(object):

    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def get_grade(self):
        if self.__score >= 90:
            return 'A-优秀'
        if self.__score >= 60 and self.__score < 90:
            return 'B-及格'
        else:
            return 'C-不及格'

p4 = Person1('Bob', 90)
p5 = Person1('Alice', 65)
p6 = Person1('Tim', 48)

print(p4.get_grade())
print(p5.get_grade())
print(p6.get_grade())