# Author:panta
# CreateDate:2019/10/31
# FileName:ValidateWord
# IDE:PyCharm

def validate_word(word, list_words):
    flag = False
    for s_word in list_words:
        s_word = s_word.rstrip()
        if word == s_word:
            flag = True
            break

    return flag


def validate_word1(word, list_words):
    word = word.rstrip()
    for s_word in list_words:
        s_word = s_word.rstrip()
        if s_word in word:
            return True
    return False
