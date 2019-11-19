# Author:panta
# CreateDate:2019/11/15
# FileName:Topic3
# IDE:PyCharm
import  numpy as np

def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y


def pair_max(a,b):
    result = []
    if isinstance(a,np.ndarray) and isinstance(b,np.ndarray):
        if len(a) == len(b):
            for i in range(len(a)):
                result.append(maxx(a[i],b[i]))

        return np.array(result)

if __name__ == '__main__':
    a = np.array([5, 7, 9, 8, 6, 4, 5])
    b = np.array([6, 3, 4, 8, 9, 7, 1])
    print(pair_max(a, b))


