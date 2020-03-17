from database1 import Connect


def main():
    no = int(input('编号: '))
    name = input('名字：')
    # 1. 创建数据库连接对象
    con = Connect.con_by_param(host='localhost', port=3306,
                               database='hrs', charset='utf8',
                               user='root', password='123456')
    try:
        with con.cursor() as cursor:
            result = cursor.execute(
                'update tb_dept set dname = %s where dno=%s',
                (name, no)
            )
            con.commit()
        if result == 1:
            print('更新成功!')
    finally:
        con.close()


if __name__ == '__main__':
    main()