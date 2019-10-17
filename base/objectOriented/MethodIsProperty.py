import types


def get_grade(self):
    return 'A'


class Person2(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score


p6 = Person2('Bob', 90)
p8 = Person2('Alice', 65)

p6.get_grade = types.MethodType(get_grade, p6)
print(p6.get_grade)
print(p6.get_grade())
print(p8.get_grade())


class Person3(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.get_grade = lambda: 'A'


p7 = Person3('Bob', 90)
print(p7.get_grade)
print(p7.get_grade())
