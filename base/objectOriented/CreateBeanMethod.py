class Person1(object):

    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def get_grade(self):
        if self.__score >= 90:
            return 'A-优秀'
        if 60 <= self.__score < 90:
            return 'B-及格'
        else:
            return 'C-不及格'

p4 = Person1('Bob', 90)
p5 = Person1('Alice', 65)
p6 = Person1('Tim', 48)

print(p4.get_grade())
print(p5.get_grade())
print(p6.get_grade())