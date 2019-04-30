# 迭代
import sys

list = [1, 2, 3, 4]

it = iter(list)

print(next(it))

for i in it:
    print(i)

# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

print("-----------------")


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myClass = MyNumbers()
print(myClass.__iter__())
myIter = iter(myClass)

print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))


# StopIteration 异常用于标识迭代完成

class MyNumbers1:
    # 构造函数
    def __init__(self, n):
        self.idx = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx <= self.n:
            x = self.idx
            self.idx += 1
            return x
        else:
            raise StopIteration


myClass1 = MyNumbers1(10)
# 创造迭代器对象
myIter1 = iter(myClass1)
for x in myIter1:
    print(x)

# 迭代器和迭代对象

print(myClass1 is iter(myClass1))
print(i for i in myClass1)
