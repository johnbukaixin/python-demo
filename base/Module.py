# import sys 引入 python 标准库中的 sys.py 模块；这是引入某一模块的方法。
import sys
from base import Support

print("输入命令行如下：")

# sys.argv 是一个包含命令行参数的列表。
for i in sys.argv:
    print(i)

# sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表。
print("\n\n系统路径为：", sys.path, '\n')

print('Python was started in 1989 by "Guido".', '\n', 'Python is free and easy to learn.')
Support.print_func("zhangsan")

print(dir())

import os

print(os.path.isdir(r'C:\Windows'))
print(os.path.isfile(r'C:\Windows\notepad.exe'))

