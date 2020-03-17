import pymysql


def con():
    # 1. 创建数据库连接对象
    con = pymysql.connect(host='localhost', port=3306,
                          database='hrs', charset='utf8',
                          user='root', password='123456')
    return con


def con_by_param(host, port, user, password, database, charset):
    if database is None or database == '':
        database = 'hrs'
    if charset is None or charset == '':
        charset = 'utf8'

    connect = pymysql.connect(host=host, port=port,
                              database=database, charset=charset,
                              user=user, password=password)
    return connect
