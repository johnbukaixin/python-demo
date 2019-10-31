# Author:panta
# CreateDate:2019/10/31
# FileName:ReplaceWord
# IDE:PyCharm
from smallTopics.ReadFileUtil import read_file

# 敏感词文本文件 TestObject.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。

def replace_word(word, list_words):
    word = word.rstrip()
    for s_word in list_words:
        s_word = s_word.rstrip()
        if s_word in word:
            rep_str = '*' * len(s_word)
            word = word.replace(s_word, rep_str)

    return word


if __name__ == '__main__':
    list_words = read_file('d:\\TestObject.txt')

    word = input('请输入词汇:')

    print(replace_word(word, list_words))
