# Author:panta
# CreateDate:2019/11/7
# FileName:lfw
# IDE:PyCharm

import tensorflow_datasets as tfds
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S')

# tfds works in both Eager and Graph modes
# tf.enable_eager_execution()

# See available datasets
print(tfds.list_builders())

# Construct a tf.data.Dataset
train_data, train_info = tfds.load(name="lfw", as_supervised=True, with_info=True,split=tfds.Split.TRAIN)

print(train_data)

mnist = tfds.load("mnist:1.*.*")

lfw_test, test_info = tfds.load("lfw", split=tfds.Split.TEST, with_info=True)
print(test_info)

fig = tfds.show_examples(test_info, lfw_test)
