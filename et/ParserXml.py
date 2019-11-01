# Author:panta
# CreateDate:2019/11/1
# FileName:ParserXml
# IDE:PyCharm

import xml.etree.ElementTree as ET
import os
from smallTopics.ReadFileUtil import read_file


def create_xml(datas, description, path, name):
    root = ET.Element('root')
    root.tail = '\n'

    students = ET.SubElement(root, 'students')
    students.tail = '\n'
    str1 = description

    students.text = str1 + '\n' + str(datas)

    tree = ET.ElementTree(root)
    save_path = os.path.join(path, name)
    tree.write(save_path, encoding="utf-8", xml_declaration=True)


if __name__ == '__main__':
    read_path = os.path.join('D:\\Users\\panta\\PycharmProjects\\demo\\openpyxl\\pri', 'student.txt')
    datas = read_file(read_path)
    description = '''
    <!-- 
        学生信息表
        "id" : [名字, 数学, 语文, 英文]
    -->
    '''

    create_xml(datas, description, 'xml', 'student.xml')
