n = 100
counter = 0
sum = 0

while counter <= 100:
    sum = sum + counter
    counter += 1

print("0到100的和为", sum)

# 死循环
# var = 1
# while var:
#     num = int(input("请输入数字："))
#     print("你输入的数字是:", num)
# print("good bye")

number = 0
while number < 5:
    print("数字小于5")
    number += 1
else:
    print("数字大于等于5了")

# for 循环
languages = ['Ruby', 'Java', 'C++', 'C', 'Python']

for i in languages:
    print(i)

websites = ['Baidu', 'Taobao', 'Tencent', 'Google']

for site in websites:
    if site == 'Tencent':
        print("Tencent")
        break
    print("循环数据", site)
else:
    print("没有循环数据")
print("完成循环")

# 遍历数字序列可以使用range内置函数 也可指定范围range(5,9) 还可以指定步长
for i in range(5):
    print(i)

for i in range(1, 50, 5):
    print(i)

# 结合range()和len()函数以遍历一个序列的索引
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(a[i])

b = list(range(5))
print(b)

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')

letter = 'Runoob'
for str in letter:
  if str == 'o':
      pass
      print("执行pass代码块")
  print(str)
print("good bye")

if None:
    print("Hello")

