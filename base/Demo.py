a, b = 0, 1
while b < 1000:
    print(b, end=' ')
    # 先计算右边表达式，然后同时赋值给左边
    # a, b = b, a + b
    n = b
    m = a + b
    a = n
    b = m
# 使用end使数据显示在同一行
