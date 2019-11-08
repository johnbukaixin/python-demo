# Author:panta
# CreateDate:2019/11/6
# FileName:Hello
# IDE:PyCharm

import cv2
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
import random
import os


# flowers = tf.keras.utils.get_file(
#     fname ='D:\\Users\\panta\\PycharmProjects\\demo\\opencv',
#     origin = 'http://vis-www.cs.umass.edu/lfw/lfw.tgz',
#     untar=True)
data_path = 'D:\\Users\\panta\\PycharmProjects\\demo\\opencv\\lfw'
img_gen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255, rotation_range=20)

images, labels = next(img_gen.flow_from_directory(data_path))
# 创建图例
plt.figure()
# 函数负责对图像进行处理，并显示其格式
plt.imshow(images[1])
# 色条
plt.colorbar()
# 显示不显示网格
plt.grid(False)
# 显示图片
plt.show()

print('images',images)
print('labels',labels)

# 注意下面数据集的划分是随机的，所以每次运行程序的训练结果会不一样
train_images, test_images, train_labels, test_labels = train_test_split(images, labels, test_size=0.3,
                                                                        random_state=random.randint(0, 100))

# 后面模型中会使用categorical_crossentropy作为损失函数，这里要对类别标签进行One-hot编码
# train_labels = tf.keras.utils.to_categorical(train_labels, 5750)
# test_labels = tf.keras.utils.to_categorical(test_labels, 5750)
# print(test_labels)  # 确认了每次都不一样
print(train_images.dtype, train_images.shape)
print(test_images.dtype, test_images.shape)
print(train_labels.dtype, train_labels.shape)
print(test_labels.dtype, test_labels.shape)
print('train_images.shape....',train_images.shape)
print('len(train_labels)....',len(train_labels))
print('train_labels....',train_labels)
print('test_images.shape.....',test_images.shape)
print('len(test_labels).....',len(test_labels))

model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=10)

test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print('\nTest accuracy:', test_acc)

predictions = model.predict(test_images)
print(predictions[0])
print(np.argmax(predictions[0]))
print(test_labels[0])





