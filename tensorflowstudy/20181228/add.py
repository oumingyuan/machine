import tensorflow as tf
import os

# 忽略警告
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

with tf.name_scope('graph') as scope:
    a = tf.constant(1, name='addend01')  # 1 row by 2 column
    b = tf.constant(2, name='addend02')  # 2 row by 1 column
    product = tf.add(a, b, name='sum')

session = tf.Session()

# tensorboard --logdir /tensorflow
tf.summary.FileWriter("/tensorflow/add", session.graph)

init = tf.global_variables_initializer()

session.run(init)
