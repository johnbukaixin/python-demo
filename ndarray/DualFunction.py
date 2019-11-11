# Author:panta
# CreateDate:2019/11/11
# FileName:DualFunction
# IDE:PyCharm

import numpy as np

a = np.arange(24).reshape((2, 3, 4))

b = np.sqrt(a)

np.maximum(a, b)
np.minimum(a, b)
np.mod(a, b)
c = a > b
