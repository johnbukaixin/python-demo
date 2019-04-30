# if-elif-else
# 使用相同缩进表示相同代码块
"""
  if condition_1:
     statement_block_1
  elif condition_2:
     statement_block_2
  else condition_3
     statement_block_3
"""

# 大于0的为True
var1 = 100
if var1:
    print("if 条件表达式为True")
    print(var1)

var2 = 0
if var2:
    print("if 条件表达式为False")
    print(var2)
print("good bye")

age = int(input("请输入你家狗狗的年龄："))

if age < 0:
    print("年龄不会小于0的")
elif age == 1:
    print("相当于14岁的人")
elif age == 2:
    print("相当于24岁的人")
elif age > 2:
    human = 22 + (age - 2) * 5
    print("相当于人的年龄：", human)

input("输入enter键退出！")

print(5 == 6)

x = 7
y = 8
print(x == y)

number = 7
guess = -1

'''
if 表达式1:
    语句
    if 表达式2:
        语句
    elif 表达式3:
        语句
    else:
        语句
elif 表达式4:
    语句
else:
    语句
'''
while number != guess:
    guess = int(input("请输入你要猜的数字："))
    if guess > number:
        print("你输入的数字太大了")
    elif guess < number:
        print("你输入的数字太小了")
    else:
        print("恭喜你答对了")

num = int(input("输入一个数字："))
if num % 2 == 0:
    if num % 3 == 0:
        print("你输入的数字可以整除 2 和 3")
    else:
        print("你输入的数字可以整除 2，但不能整除 3")
else:
    if num % 3 == 0:
        print("你输入的数字可以整除 3，但不能整除 2")
    else:
        print("你输入的数字不能整除 2 和 3")
