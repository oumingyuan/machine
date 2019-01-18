import tensorflow as tf
import numpy as np

# 用Tensorflow计算a=(b+c)∗(c+2)

# d=b+c
# e=c+2
# a=d*e
const = tf.constant(2.0, name='const')

# b = tf.Variable(2.0, dtype=tf.float32, name='b')
# 创建placeholder
b = tf.placeholder(tf.float32, [None, 1], name='b')

c = tf.Variable(1.0, dtype=tf.float32, name='c')

d = tf.add(b, c, name='d')
e = tf.add(c, const, name='e')
a = tf.multiply(d, e, name='a')

# 1. 定义init operation
init_op = tf.global_variables_initializer()

# session
with tf.Session() as sess:
    # tensorboard --logdir /tensorflow/math
    writer = tf.summary.FileWriter("/tensorflow/math", sess.graph)

    init = tf.global_variables_initializer()

    # 2. 运行init operation
    sess.run(init_op)
    # 计算
    # a_out = sess.run(a)
    a_out = sess.run(a, feed_dict={b: np.arange(0, 10)[:, np.newaxis]})
    print("Variable a is {}".format(a_out))
