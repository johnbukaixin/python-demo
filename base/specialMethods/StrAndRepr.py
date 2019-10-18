class Person(object):

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Student(Person):

    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

    def __str__(self):
        return '<(student: %s, %s, %s)>' % (self.name, self.gender, self.score)


s = Student('Bob', 'male', 88)
print(s)

import functools


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return '(%s: %s)' % (self.name, self.score)

    __repr__ = __str__

    def cmp(self, s):
        if isinstance(s, Student):
            if self.score > s.score:
                return -1
            if self.score < s.score:
                return 1

            else:
                if self.name > s.name:
                    return 1
                elif self.name < s.name:
                    return -1
                else:
                    return 0


L = [Student('Tim', 99), Student('Bob', 88), Student('Alice', 99)]
print(sorted(L, key=functools.cmp_to_key(Student.cmp)))

print(sorted(L, key=lambda s: (-s.score, s.name)))


class Fib(object):
    def __init__(self, num):
        a, b, L = 0, 1, []
        for n in range(num):
            L.append(a)
            a, b = b, a + b
        self.num = L

    def __str__(self):
        return str(self.num)

    __repr__ = __str__

    def __len__(self):
        return len(self.num)

f = Fib(10)
print(f)
print(len(f))

a,b = 1,2
print(a,b)