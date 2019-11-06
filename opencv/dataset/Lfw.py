# Author:panta
# CreateDate:2019/11/6
# FileName:Lfw
# IDE:PyCharm
import os
import cv2
import logging

data_array, labels_array = [], []


def load_data(path_name):
    if os.path.isdir(path_name):
        files = os.listdir(path_name)
        for file in files:
            path = os.path.join(path_name, file)
            print(path)
            if os.path.isfile(path):
                try:
                    img_data = cv2.imread(path)
                    data_array.append(img_data)
                    labels_array.append(file.split('.')[0])
                except Exception as e:
                    logging.error("加载数据错误,路径{0}", os.path.abspath(file), e)
            else:
                load_data(path)
    return data_array, labels_array


def reset_size(data_array, width, height):
    pass


if __name__ == '__main__':
    data_array, labels_array = load_data('D:\\Users\\panta\\PycharmProjects\\demo\\opencv\\lfw')
    print(data_array)
    print(labels_array)
