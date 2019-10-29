# Author:panta
# CreateDate:2019/10/25
# FileName:CountlinesCode
# IDE:PyCharm

import os


def read_file(file_path):
    """
    :param file_path: 要读取的文件夹路径
    :return:
    """
    if file_path == '' or file_path is None:
        print('文件路径不能为空')
        return
    try:
        if not os.path.isfile(file_path):
            files = os.listdir(file_path)
            for file in files:
                path = os.path.join(file_path, file)
                if os.path.isfile(path):
                    f = open(path, 'r+', encoding="ISO-8859-1")
                    # 读取全部内容
                    codes = f.readlines()
                    print(file, count(codes))
                else:
                    read_file(path)
        else:
            f = open(file_path, 'r+', encoding="ISO-8859-1")
            codes = f.readlines()
            print(file_path, count(codes))
    except Exception as  error:
        print("出现如下异常%s" % error)


def count(codes):
    flag = False
    comment_lines = 0
    code_lines = 0
    blank_lines = 0
    for code in codes:
        code = code.rstrip()
        if not flag:
            if validate_annotation(code):
                flag = True
                comment_lines += 1
            elif code.startswith("#"):
                comment_lines += 1
            elif validate_blank_line(code):
                blank_lines += 1
            else:
                code_lines += 1

        # 已经开始，结束注释
        else:
            if code.endswith("'''") or code.endswith('"""'):
                flag = False
                comment_lines += 1
            else:
                comment_lines += 1

    return code_lines, comment_lines, blank_lines


def validate_annotation(code):
    if isinstance(code, str):
        if code == '"""' or code == "'''":
            return True

    return False


def validate_blank_line(code):
    if isinstance(code, str):
        code.strip()
        if code == "":
            return True
    return False


if __name__ == '__main__':
    read_file("D:\\Users\\panta\\PycharmProjects\\demo\\base")
