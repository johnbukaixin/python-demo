# Author:panta
# CreateDate:2019/11/7
# FileName:DataSet
# IDE:PyCharm

import random

from opencv.dataset.Lfw import load_data
from tensorflow import keras
from sklearn.model_selection import train_test_split



class dataSet(object):
    def __init__(self, path_name):
        self.train_faces = None
        self.train_labels = None
        self.test_face = None
        self.test_labels = None
        self.path_name = path_name
        self.input_shape = None

    # 加载数据集并按照交叉验证的原则划分数据集并进行相关预处理工作
    def load(self, img_rows, img_cols, img_channels=3, nb_classes=2):
        # 加载数据集到内存
        images, labels = load_data(self.path_name)

        # 注意下面数据集的划分是随机的，所以每次运行程序的训练结果会不一样
        train_images, test_images, train_labels, test_labels = train_test_split(images, labels, test_size=0.3,random_state=random.randint(0, 100))
        print(test_labels) # 确认了每次都不一样

        # tensorflow 作为后端，数据格式约定是channel_last，与这里数据本身的格式相符，如果是channel_first，就要对数据维度顺序进行一下调整
        if keras.backend.image_data_format == 'channel_first':
            train_images = train_images.reshape(train_images.shape[0], img_channels, img_rows, img_cols)
            test_images = test_images.reshape(test_images.shape[0], img_channels, img_rows, img_cols)
            self.input_shape = (img_channels, img_rows, img_cols)
        else:
            train_images = train_images.reshape(train_images.shape[0], img_rows, img_cols, img_channels)
            test_images = test_images.reshape(test_images.shape[0], img_rows, img_cols, img_channels)
            self.input_shape = (img_rows, img_cols, img_channels)

        # 输出训练集和测试集的数量
        print(train_images.shape[0], 'train samples')
        print(test_images.shape[0], 'test samples')

        # 后面模型中会使用categorical_crossentropy作为损失函数，这里要对类别标签进行One-hot编码
        train_labels = keras.utils.to_categorical(train_labels, nb_classes)
        test_labels = keras.utils.to_categorical(test_labels, nb_classes)

        # 图像归一化，将图像的各像素值归一化到0~1区间。
        train_images /= 200
        test_images /= 200

        self.train_faces = train_images
        self.test_face = test_images
        self.train_labels = train_labels
        self.test_labels = test_labels



if __name__ == '__main__':
    dataSet = dataSet('D:\\Users\\panta\\PycharmProjects\\demo\\opencv\\lfw1')

    dataSet.load(64,64)
