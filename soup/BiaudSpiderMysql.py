
from database1 import Connect
from hashlib import sha1
from urllib.parse import urljoin

import pickle
import re
import requests
import zlib
import base64

from bs4 import BeautifulSoup

def main():
    # 指定种子页面
    base_url = 'https://www.zhihu.com/'
    seed_url = urljoin(base_url, 'explore')
    # 创建Redis客户端
    con = Connect.con_by_param(host='localhost', port=3306,
                               database='hrs', charset='utf8',
                               user='root', password='123456')
    # 设置用户代理(否则访问会被拒绝)
    headers = {'user-agent': 'Baiduspider'}
    # 通过requests模块发送GET请求并指定用户代理
    resp = requests.get(seed_url, headers=headers)
    # 创建BeautifulSoup对象并指定使用lxml作为解析器
    soup = BeautifulSoup(resp.text, 'html.parser')
    href_regex = re.compile(r'^/question')
    # 将URL处理成SHA1摘要(长度固定更简短)
    hasher_proto = sha1()
    # 查找所有href属性以/question打头的a标签
    for a_tag in soup.find_all('a', {'href': href_regex}):
        # 获取a标签的href属性值并组装完整的URL
        href = a_tag.attrs['href']
        full_url = urljoin(base_url, href)
        # 传入URL生成SHA1摘要
        hasher = hasher_proto.copy()
        hasher.update(full_url.encode('utf-8'))
        field_key = hasher.hexdigest()
        # 如果Redis的键'zhihu'对应的hash数据类型中没有URL的摘要就访问页面并缓存
        if not select_by_id(con,field_key) :
            html_page = requests.get(full_url, headers=headers).text
            # 对页面进行序列化和压缩操作
            zipped_page = zlib.compress(pickle.dumps(html_page))
            final_data = base64.b64encode(zipped_page)
            # 使用hash数据类型保存URL摘要及其对应的页面代码
            add(con,field_key, final_data)
    # 显示总共缓存了多少个页面
    # print('Total %d question pages found.' % client.hlen('zhihu'))

def select_by_id(con,id):
    with con.cursor() as cursor:
        cursor.execute(
            'select * from tb_zhihu where id=%s',
            (id,)
        )
        result = cursor.fetchall()
    return result

def add(con,id,content):
    with con.cursor() as cursor:
        result = cursor.execute(
            'insert into tb_zhihu values (%s,%s)',
            (id, content)
        )

        if result == 1:
            return result

if __name__ == '__main__':
    main()