class Person4(object):
    __count = 0

    def __init__(self, name):
        self.name = name
        Person4.__count = Person4.__count + 1

    @classmethod
    def how_many(cls):
        return cls.__count


print(Person4.how_many())

p9 = Person4('Bob')

print(Person4.how_many())