# 列表
list1 = [1, 2, 35.56, 78, 80]
# [1, 2, 35.56, 'ddd', 78, 80]
list1.insert(3, 'ddd')
print(list1)

# [1, 2, 35.56, 'ddd', 78, 80, 'eee']
list1.append("eee")
print(list1)

# [1, 2, 35.56, 'ddd', 78, 80, 'eee', 3, 567, 7]
list1.extend([3, 567, 7])
print(list1)

# [1, 2, 35.56, 78, 80, 'eee', 3, 567, 7]
list1.pop(3)
print(list1)

list1.insert(0, "test")
# ['test', 1, 35.56, 78, 80, 'eee', 3, 567, 7]
list1.remove(2)
print(list1)

# 1 统计次数
print(list1.count(1))

# [7, 567, 3, 'eee', 80, 78, 35.56, 1, 'test']
list1.reverse()
print(list1)

# 5
print(list1.index(78))

# 集合、字典等

# 遍历技巧
# 字典遍历
knignt = {'gallahad': 'the pure', 'robin': 'the brave'}
for i, v in knignt.items():
    print(i, v)

# 序列遍历时 使用enumerate()同时输出index，value
klist = ["sss", "ccc", "fff"]
for i, v in enumerate(klist):
    print(i, v)

# 同时遍历两个或多个序列时，可以使用zip
alist = ['ddd', 'fff', 'gggg']
blist = ['eee', 'bbb', 'jjj']
for i, v in zip(alist, blist):
    print('What is your {0}?  It is {1}.'.format(i, v))

# 反向遍历
for v in reversed(range(1, 9)):
    print(v)
