# Author:panta
# CreateDate:2019/10/30
# FileName:FindBody1
# IDE:PyCharm

import urllib.request
from bs4 import BeautifulSoup

url = "https://www.mytijian.com"
page = urllib.request.urlopen(url)

soup = BeautifulSoup(page,'lxml')
print(soup.body.text)