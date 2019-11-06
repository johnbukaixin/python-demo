# Author:panta
# CreateDate:2019/11/6
# FileName:Hello
# IDE:PyCharm

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('D:\\Users\\panta\\PycharmProjects\\demo\\opencv\\lfw\\Aaron_Eckhart\\Aaron_Eckhart_0001.jpg', 0)

# 创建图例
plt.figure()
# 函数负责对图像进行处理，并显示其格式
plt.imshow(img)
# 色条
plt.colorbar()
# 显示不显示网格
plt.grid(False)
# 显示图片
plt.show()
