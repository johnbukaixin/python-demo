# Author:panta
# CreateDate:2019/10/30
# FileName:__Call__
# IDE:PyCharm

class Fib(object):
    def __call__(self, num):
        if num == 1 or num == 2:
            return 1
        else:
            return self.__call__(num - 1) + self.__call__(num - 2)



f = Fib()
print(f(20))

class Fib1(object):
    L = []
    def __call__(self, num):
        a, b, L = 0, 1, []
        for n in range(num):
            L.append(a)
            a, b = b, a + b
        return L



f = Fib1()
print(f(10))