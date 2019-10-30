# Author:panta
# CreateDate:2019/10/29
# FileName:FindoutBody
# IDE:PyCharm

# 一个HTML文件，找出里面的正文。

import os

from smallTopics.ReadFileUtil import read_file


def read_dir(file_path):
    """
        :param file_path: 要读取的文件夹路径
        :return:
        """
    if file_path == '' or file_path is None:
        print('文件路径不能为空')
        return
    try:
        L = []
        if not os.path.isfile(file_path):
            files = os.listdir(file_path)
            for file in files:
                L.append(read_file(file_path, file))
        else:
            L.append(read_file(file_path))

        return L
    except Exception as  error:
        print("出现如下异常%s" % error)




def find_body(codes, flag):
    is_body = False

    if isinstance(codes, str):
        if not flag:
            if codes == '<body>\n' or codes == '<BODY>\n':
                flag = True
                is_body = True
        else:
            if codes == '</body>\n' or codes == '</BODY>\n':
                flag = False
                is_body = True
            else:
                is_body = True
    return is_body, flag


if __name__ == '__main__':
    L = read_dir("D:\\work\\ttt.html")
    body = []
    flag = (False, False)

    for code in L:
        if isinstance(code, list):
            for c in code:
                flag = find_body(c, flag[1])
                if flag[0]:
                    body.append(c)
    print(body)
