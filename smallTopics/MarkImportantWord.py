# Author:panta
# CreateDate:2019/10/25
# FileName:MarkImportantWord
# IDE:PyCharm
import os
import re


def read_file(file_path):
    """
    :param file_path: 要读取的文件夹路径
    :return:
    """
    if file_path == '' or file_path is None:
        print('文件路径不能为空')
        return
    try:
        files = os.listdir(file_path)
        for file in files:
            if not os.path.isdir(file):
                f = open(file_path + '\\' + file)
                diary = f.read()
                L = mark_import_word(diary, ["Python", "enthusiastic", "knowledgebase"])
                print(len(L))
    except Exception as  error:
        print("出现如下异常%s" % error)


def mark_import_word(content, import_words):
    """
    :param content:  需要标记的内容
    :param import_words: 你认为重要的单词
    :return:
    """
    L = []
    if not isinstance(import_words, list):
        print('重要词汇格式不正确')
    contents = re.split(r'[;,\s]', content)
    for word in contents:
        if word in import_words:
            L.append(word)

    return L


if __name__ == '__main__':
    read_file("d:\\diary")
