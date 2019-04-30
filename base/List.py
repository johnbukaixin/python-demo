x = ['a', 'b', 1]
y = [2, 3, 4]
z = ['ss', 'd', 5]

print(len(x))
w = [x, y, z]
print(w)
print(w[1])
print(w[1][0])

# 在列表末尾追加
x.append("z")
print(x)
print(x.index(1))
# 没有返回值 在原有列表后面一次性追加另一个序列中的多个值 无返回值
x.extend((2, 3))
print(x)
# 在索引为1（index）的位置插入obj 无返回值
y.insert(1, "d=v")
print(y)

# 移除位置为1的元素 返回值为空，操作对象
y.pop(1)
print(y)
# 移除最后一个
y.pop()
print(y)
# 移除第一个匹配的 无返回值
y.remove(2)
print(y)

# 列表翻转 直接操作对象 无返回值
z.reverse()
print(z)
# 只支持同类型排序，否则会报错 无返回值
z.sort()
print(z)