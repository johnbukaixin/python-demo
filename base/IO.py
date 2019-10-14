strq = input("请输入:")

print("您输入的是：", strq)


# 打开一个文件
f = open("d://tmp//foo.txt", "a")
# 可以返回写入的字符数
num = f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
print(num)




# 如果不是str 需要转先str，再写入文件
new_value = ('haha',4)

value = str(new_value)

f.write(value)

f.close()

# 打开一个文件
f = open("d://tmp//foo.txt", "r")

strq = f.read()
print(strq)

f.close()

f = open("d://tmp//foo.txt", "rb+")
new_num = f.write(b"dandruff ")

print(new_num)

# 移动文件到第四个字节
f.seek(3)

# 从3开始读两个字节
print(f.read(2))

f.seek(-3,2) # 移动到文件的倒数第三字节

print(f.read(1))

