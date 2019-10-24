#  你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
from PIL import Image
import os
import string
import random

def change_image_size(image_file_path):
    """
    :param image_file_path: 存放需要处理图片文件夹
    :return:
    """
    if image_file_path == '' or image_file_path is None:
        print('文件路径不能为空')
        return
    try:
        files = os.listdir(image_file_path)
        for file in files:
            try:
                if not os.path.isdir(file):
                    img = Image.open(image_file_path + '\\' + file)
                    iphone5_width = 1136
                    iphone5_depth = 640
                    change_size_out((iphone5_width, iphone5_depth), img)
            except Exception  as OSError:
                print("出现如下异常%s" % OSError)



    except FileNotFoundError:
        print('文件找不到')


def change_size_out(depth_width, img):
    """
    :param depth_width: 图片目标长度，宽度（100，100）
    :param img: Image类型
    :return:
    """
    if not isinstance(depth_width, tuple) and len(depth_width) == 2:
        print("请输入合格期望的图片分辨率，以元组的形式(长，宽)。。。。")
        return
    if img is Image:
        return
    target_depth = depth_width[0]
    target_width = depth_width[1]
    img.thumbnail((target_width, target_depth))
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 20))
    is_exists = os.path.exists("image")
    if not is_exists:
        os.makedirs("image")

    img.save('image\\finish_' + ran_str + '.jpg', 'png')


# iphone5_width=1136
# iphone5_depth=640
if __name__ == '__main__':
    change_image_size("D:\\work\\图片")
