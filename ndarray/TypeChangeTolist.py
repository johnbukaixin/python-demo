# Author:panta
# CreateDate:2019/11/14
# FileName:TypeChangeTolist
# IDE:PyCharm
import numpy as np

# astype()方法先创建新的数组（原始数据的拷贝），鸡是两个类型一致
ones = np.ones((2,3,4),dtype = np.int)
print('ones----->',ones)
b_ones = ones.astype(np.float)
print('b_ones----->',b_ones)



full = np.full((2,3,4),34,dtype = np.int32)
print('full--->',full)

full_list = full.tolist()
print('full_list---->',full_list)