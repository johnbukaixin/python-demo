# Author:panta
# CreateDate:2019/10/31
# FileName:DownloadImage
# IDE:PyCharm
import urllib.request
import logging
from bs4 import BeautifulSoup


def download_image(url, parser, tag, src, pageNum):
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
        new_url = url + str(page) + '.html'
        logging.info(new_url)
        page = urllib.request.urlopen(new_url)
        soup = BeautifulSoup(page, parser)
        imgs = soup.find_all(tag)
        for img in imgs:
            try:
                src = img.get(src)
                if not src is None:
                    urllib.request.urlretrieve(src, "img/%02d." % imgID + src[-3:])
                    imgID += 1
            except Exception as e:
                logging.exception(e)


if __name__ == '__main__':
    url = 'https://www.fabiaoqing.com/bqb/lists/type/hot/page/'

    download_image(url, 'lxml', 'img', 'data-original', 1003)
