# Author:panta
# CreateDate:2019/11/19
# FileName:Topic4
# IDE:PyCharm
import numpy as np

# Create a custom dtype that describes a color as four unsigned bytes (RGBA) (★☆☆)
# 创建一个自定义dtype，将颜色描述为四个无符号字节（RGBA）创建一个自定义dtype，将颜色描述为四个无符号字节（RGBA）

color = np.dtype([('r', np.ubyte), ('g', np.ubyte), ('b', np.ubyte), ('a', np.ubyte)])

print(color)


a = np.ones((5,3))
b = np.ones((3,2))

print(np.dot(a,b))