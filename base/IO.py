str = input("请输入:")

print("您输入的是：", str)


# 打开一个文件
f = open("d://tmp//foo.txt", "w")

f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )

# 关闭打开的文件
f.close()