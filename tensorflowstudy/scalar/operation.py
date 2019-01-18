import tensorflow as tf

# 定义两个占位符a和b，将接收接下来要相加、乘的两个标量2，3
a = tf.placeholder(tf.int16)
b = tf.placeholder(tf.int16)

# 启动计算图
# 其中 add为加操作，mul为乘操作，a和b接收数据，feed_dict将数据输入到计算图中
# sess.run 运行计算图
with tf.Session() as sess:
    print("Addition with variables: %i" % sess.run(add, feed_dict={a: 2, b: 3}))
    print("Multiplication with variables: %i" % sess.run(mul, feed_dict={a: 2, b: 3}))
