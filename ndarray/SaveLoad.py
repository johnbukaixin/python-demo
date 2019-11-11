# Author:panta
# CreateDate:2019/11/11
# FileName:SaveLoad
# IDE:PyCharm

import numpy as np

a = np.arange(6).reshape(2,3)
# 保存数据
np.savetxt('a.csv',a,fmt='%d',delimiter=',')
np.savetxt('1f.csv',a,fmt='%.1f',delimiter=',')

# frame 文件、字符串，
b = np.loadtxt('a.csv',delimiter=',')
print(b)
c = np.loadtxt('a.csv',dtype=np.int,delimiter=',')
print(c)

save1 = np.arange(100).reshape(5,10,2)
save1.tofile('save1.bat',sep=',',format='%d')

np.fromfile('save1.bat',sep=',').reshape(5,10,2)

save1.tofile('save2.bat',format='%d')

np.fromfile('save2.bat',dtype = np.int).reshape(5,10,2)

np.save('np_save.npy',save1)
np.load('np_save.npy')
