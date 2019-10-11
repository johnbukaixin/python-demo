# 字典类似json kv键值对 k不可变的类型并且不重复，区分大小写，v可变，并且可重复
dict1 = {"a": "haha", "b": 1, "c": "hdsjhj"}
dict2 = {'abc': 123, 98.6: 37}

print(dict1["a"])

dict1["a"] = "ssss"
print(dict1)
dict1["d"] = 'ccccc'
print(dict1)
del dict1["d"]
print(dict1)

print(len(dict1))
print(str(dict1))

# 清空是清除字典中的数据
dict1.clear()
print(dict1)
# 删除是直接删除对象
# del dict1
# print(dict1)

dict1 = {'user': 'runoob', 'num': [1, 2, 3]}
dict2 = dict1  # 浅拷贝: 引用对象
dict3 = dict1.copy()  # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用（两者结合起来为浅拷贝）
# 修改 data 数据
dict1['user'] = 'root'
dict1['num'].remove(1)
# 输出结果
# {'user': 'root', 'num': [2, 3]}
print(dict1)
# {'user': 'root', 'num': [2, 3]}
print(dict2)
# {'user': 'runoob', 'num': [2, 3]}
print(dict3)

# 实例中 dict2 其实是 dict1 的引用（别名），所以输出结果都是一致的，dict3 父对象进行了深拷贝，不会随dict1 修改而修改，子对象是浅拷贝所以随 dict1 的修改而修改。

copydcit = dict1.copy()
print(copydcit)
# {'d': 10, 'c': 10}
newDict = dict1.fromkeys(["d", "c", "d"], 10)
# {'d': None, 'c': None}
newDict1 = dict1.fromkeys(["d", "c", "d"])
print(newDict)
print(newDict1)

print(newDict.get("d"))

# False
print("d" in dict1)
# True
print("d" in newDict)

# 返回可遍历的(键, 值) 元组数组 dict_items([('user', 'root'), ('num', [2, 3])])
print(dict1.items())
# 返回键 返回一个迭代器
dict1.keys()
# 转换成一个列表
list(dict1.keys())

newDict.setdefault("s", "张三")
print(newDict)
newDict.setdefault("d", "张三")
print(newDict)

# {'user': 'root', 'num': [2, 3], 'd': 10, 'c': 10, 's': '张三'} newDict中的键/值对更新到dict1里
dict1.update(newDict)
print(dict1)
# 张三 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
print(dict1.pop("s"))


d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

sum = 0.0
for k, v in d.items():
    sum = sum + v
    print (k,':',v)
print ('average', ':', sum / len(d.items()))
