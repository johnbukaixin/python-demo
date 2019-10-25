#  做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？
import random
import string

ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))

print(ran_str)

print(string.capwords(ran_str))
print('a'.join([i.capitalize() for i in ran_str.split('a')]))

# capwords = 'a'.join([i.capitalize() for i in ran_str.split('a')])
print(random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()'))

print(random.sample('zyxwvutsrqponmlkjihgfedcba', 5))


# 解答：
def generateActivationCode():
    L = []
    for i in range(200):
        ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 20))
        L.append(ran_str)

    return L


L = generateActivationCode()
print(L)


# 第 0002 题: 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

import pymysql

# 打开数据库连接（ip/数据库用户名/登录密码/数据库名）
db = pymysql.connect("localhost", "root", "root", "python_test")
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# L = generateActivationCode()
#
# for code in L:
#     ran_str = "insert into tb_active_code (`code`) values ('" + code + "')"
#     cursor.execute(ran_str)
#
#     db.commit()

str_sql = "select * from tb_active_code"
cursor.execute(str_sql)
results = cursor.fetchall()

for row in results:
    ran_str = row[0]
    print(ran_str)
# 关闭数据库连接
db.close()
