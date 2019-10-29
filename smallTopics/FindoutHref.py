# Author:panta
# CreateDate:2019/10/29
# FileName:FindoutHref
# IDE:PyCharm

# todo: 判断链接
from smallTopics.FindoutBody import read_dir


def validate_href(code):
    if isinstance(code,str):
        if code.startswith("<a href"):
            return True

    return False


def find_href(code):
    if isinstance(code,list):
        for c in code:
            if isinstance(c,list):
                find_href(c)
            else:
                is_href = validate_href(c)
                return is_href,c

    return False,code


if __name__ == '__main__':
    codes = read_dir("D:\\work\\ttt.html")
    href = []

    result = find_href(codes)
    if result[0]:
        href.append(result[1])

    print(href)


