# 不重复元素
set1 = {"apple", "banana", "orange", "pear", "banana"}
# 集合去重
print(set1)

# 判断在不在集合中
print("apple" in set1)

set2 = set('000absdjkdjkd')
print(set2)
set3 = set('ssssdjhfdjhfj0')
print(set3)
# 集合a中包含而集合b中不包含的元素
print(set2 - set3)
# 集合a或b中包含的所有元素
print(set3 | set2)
# 集合a和b中都包含了的元素
print(set3 & set2)
# 不同时包含于a和b的元素
print(set3 ^ set2)

set2.add("c")
print(set2)
# 添加元素，且参数可以是列表，元组，字典 还可以支持多个
set2.update({"m", "v"}, {"r", "i"})
print(set2)

set1.remove("apple")
print(set1)

# 不存在会报错
# set1.remove("haha")
# 不存在不会报错
set1.discard("haha")

# 脚本模式中注释随机删除一个 交互模式中是删除第一个
set1.pop()

print("orange" in set1)

print(set1.isdisjoint(set2))

# 判断 set2 是否是set1的子集
print(set3.issubset(set1))
# 判断set1是否是set2的子集
print(set3.issuperset(set1))