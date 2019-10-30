# Author:panta
# CreateDate:2019/10/30
# FileName:FindWords
# IDE:PyCharm
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
