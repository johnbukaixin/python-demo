string = "hello world"
capitalize = string.capitalize()
print(capitalize)
center_string = string.center(5, "5")
print(center_string)

sub = 'haha'
# 2
count = sub.count("a", 0, 4)
print(count)

test = r'''
  '\"To be, or not to be\": that is the question.\nWhether it\'s nobler in the mind to suffer.'
'''

test1 = '''
  \"To be, or not to be\": that is the question.\nWhether it\'s nobler in the mind to suffer.
'''

print('''
  静夜思

床前明月光，
疑是地上霜。
举头望明月，
低头思故乡。 
''')


print(test)
print(test1)
str = "菜鸟教程"
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")
print(str)
print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)
print("UTF-8 解码：", str_utf8.decode('UTF-8', 'strict'))
print("GBK 解码：", str_gbk.decode('GBK', 'strict'))

# True
boolean1 = str.endswith("程", 0, 4)
print(boolean1)
# True
boolean = str.startswith("菜", 0, 4)
print(boolean)

index1 = str.find("d", 0, 4)
# -1
print(index1)
# 0
index2 = str.find("菜", 0, 4)
print(index2)
# 0
index3 = str.index("菜", 0, 2)
print(index3)

numberStr = "123456"
# True
print(numberStr.isnumeric())
# True
print(numberStr.isdigit())
# False
print(numberStr.isalpha())
numberStra = "ssssss"
# True
print(numberStra.isalpha())

seq = ("s", "b")
ha = 'a'
# sab
join_str = ha.join(seq)
print(join_str)
# 3
print(len(join_str))
# s
print(max(join_str))
# a
print(min(join_str))
