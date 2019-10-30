# Author:panta
# CreateDate:2019/10/30
# FileName:ReadFileUtil
# IDE:PyCharm
import os


def read_file(file_path, file=None):
    if file is None or file == '':
        path = file_path
    else:
        path = os.path.join(file_path, file)

    if os.path.isfile(path):
        f = open(path, 'r+', encoding="UTF-8")
        # 读取全部内容
        codes = f.readlines()
        return codes
    else:
        read_file(file_path, file)
