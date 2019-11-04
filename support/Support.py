def print_func(name):
    print("hello!, ", name)


import os
import time


def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕上的输出
        os.system('cls')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


# 该返回的是 lamba函数list
def num():
    return [lambda x: i * x for i in range(4)]


print(num())
print([m(5) for m in num()])


def func(a, b=[]):
    b.append(a)
    print(b)


if __name__ == '__main__':
    for i in range(3):
        func(i)
