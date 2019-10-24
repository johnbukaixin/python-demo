# 第 0004 题： 任一个英文的纯文本文件，统计其中的单词出现的个数。

def statistics_num(eng_str):
    """
    :param eng_str: 需要统计的英文字符串
    :return:
    """
    L = list(eng_str)
    count = 0
    for sub_str in L:
        if isinstance(sub_str, str):
            if sub_str.isalpha():
                count += 1
    return count


def statistics_english_frequency(file_path):
    """
    :param file_path: 目标文件路径
    :return:
    """
    if file_path == '' or file_path is None:
        print('文件路径不能为空')
        return
    try:
        f = open(file_path, 'r+', encoding='UTF-8')
        eng_str = f.read()
        count = statistics_num(eng_str)
        print(count)
    except FileNotFoundError:
        print('文件找不到')


if __name__ == '__main__':
    statistics_english_frequency("d:\\TestObject.txt")
    statistics_english_frequency("")
    statistics_english_frequency("d:\\TestObjec.txt")
