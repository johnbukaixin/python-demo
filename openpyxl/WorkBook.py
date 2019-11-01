# Author:panta
# CreateDate:2019/11/1
# FileName:WorkBook
# IDE:PyCharm

import json
import os

from openpyxl import Workbook
from openpyxl import load_workbook

from smallTopics.ReadFileUtil import read_file


def create_work_book(name, path, sheet_names):
    wb = Workbook()
    ws = wb.active
    if isinstance(sheet_names, list):
        ws.title = sheet_names[0]
        for index, sheet_name in enumerate(sheet_names):
            if index == 0:
                continue
            wb.create_sheet(sheet_name)

    save_path = os.path.join(path, name)
    wb.save(save_path)


def txt_change_work_book(lines, path, index=0):
    if path is None or path == '':
        create_work_book('default.xlsx', os.getcwd(), 'default')
        default_path = os.path.join(os.getcwd(), "default.xlsx")
        write_work_book(default_path, index, lines)

    if not os.path.exists(path):
        s_path, file = os.path.split(path)
        file_name = file.split('.')[0]
        file_names = [file_name]
        create_work_book(file, s_path, file_names)

    if os.path.isfile(path):
        is_work_book = validate_file_is_work_book(path)
        if not is_work_book:
            print('文件类型不正确')
            raise FileNotFoundError
        write_work_book(path, index, lines)

    if os.path.isdir(path):
        create_work_book('default.xlsx', path, 'default')
        default_path = os.path.join(path, "default.xlsx")
        write_work_book(default_path, index, lines)


def write_work_book(path, index, lines):
    wb = load_workbook(path)
    sheet_names = wb.get_sheet_names()
    # index，默认为0 index为0为第一张表
    ws = wb[sheet_names[index]]
    if isinstance(lines, dict):
        number = list(lines.keys())
        datas = list(lines.values())
        for row in range(len(number)):
            # dict中的key写在第一列
            ws.cell(column=1, row=row + 1, value=number[row])

        for data_key, rows in enumerate(datas):
            if isinstance(rows, list):
                for row_key, value in enumerate(rows):
                    # 从第二列开始写数据
                    ws.cell(column=row_key + 2, row=data_key + 1, value=value)
            else:
                ws.cell(column=2, row=data_key + 1, value=rows)
    elif isinstance(lines, list):
        for row in range(len(lines)):
            ws.append(lines[row])

    wb.save(filename=path)


def validate_file_is_work_book(path):
    dir = path.split('.')
    if len(dir) >= 2:
        file_type = dir[len(dir) - 1]
        if file_type == 'xlsx':
            return True
    return False


if __name__ == '__main__':
    read_path = os.path.join('pri', 'numbers.txt')
    read_lines = read_file(read_path)
    new_lines = []

    for line in read_lines:
        line = line.rstrip()
        new_lines.append(line)

    new_lines = ''.join(new_lines)
    lines = json.loads(new_lines)

    txt_change_work_book(lines, os.path.join('excel', 'numbers.xlsx'))
