# Author:panta
# CreateDate:2019/10/30
# FileName:FindWords
# IDE:PyCharm

# 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
# 北京
# 程序员
# 公务员
# 领导
# 牛比
# 牛逼
# 你娘
# 你妈
# love
# sex
# jiangge
from smallTopics.ReadFileUtil import read_file


def validate_word(word, list_words):
    flag = False
    for s_word in list_words:
        s_word = s_word.rstrip()
        if word == s_word:
            flag = True
            break

    if flag:
        print('Freedom')
    else:
        print('Human Rights')


if __name__ == '__main__':
    list_words = read_file('d:\\TestObject.txt')

    word = input('请输入词汇:')

    validate_word(word, list_words)
