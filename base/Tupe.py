tup1 = ("d", "f", "e")
tup2 = (1, 2, "w")
tup3 = "1", "2", "3"
print(type(tup3))
# 空元组
tup4 = ()
tup = (2)
print(type(tup))
tup = (2,)
print(type(tup))

for x in tup1:
    print(x,)

print("d" in tup1)

print(tup * 4)