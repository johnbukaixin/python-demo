# Author:panta
# CreateDate:2019/10/30
# FileName:FindBody1
# IDE:PyCharm
import urllib.request
from bs4 import BeautifulSoup
import time

User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
header = {}
header['User-Agent'] = User_Agent

def find_href():
    url = "https://www.mytijian.com"
    req = urllib.request.Request(url, headers=header)
    page = urllib.request.urlopen(req)

    soup = BeautifulSoup(page, 'lxml')
    links = soup.findAll('a')
    for link in links:
        print(link['href'])



if __name__ == '__main__':
    for i in range(100000):
        find_href()
        time.sleep(1)