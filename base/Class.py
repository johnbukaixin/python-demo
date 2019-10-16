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
