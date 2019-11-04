# Author:panta
# CreateDate:2019/11/4
# FileName:Lianjia
# IDE:PyCharm

import urllib.request
import logging
from bs4 import BeautifulSoup
import random


def download_image(url, parser, tag, _class, pageNum):
    """
    :param url: 访问路径 https://www.fabiaoqing.com/bqb/lists/type/hot/page/
    :param parser: 解析器
    :param tag: 访问tag
    :param src: 获取资源的属性名称
    :param pageNum: 网页的总页数
    :return:
    """

    imgID = 0
    for page in range(1, pageNum):

        headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0'}

        new_url = url + 'pg' + page
        # urllib.request.Request（）用于向服务端发送请求，就如 http 协议客户端向服务端发送请求 POST
        # 添加了一个头部，伪装成浏览器,此时的url并不是一个裸露的url，而是具有header头部的url
        req = urllib.request.Request(url=url, headers=headers)

        # urllib.request.urlopen（）则相当于服务器返回的响应,返回的是一个request类的一个对象， GET
        # 类似于一个文件对象，可以进行ｏｐｅｎ()操作获取内容
        page = urllib.request.urlopen(req)
        soup = BeautifulSoup(page, parser)
        tags = soup.find_all(tag, class_=_class)
        for tag in tags:
            try:
                print(tag.contents)
            except Exception as e:
                logging.exception(e)


if __name__ == '__main__':
    url = 'https://hh.fang.ke.com/loupan/'

    download_image(url, 'lxml', 'span', 'number', 7)
