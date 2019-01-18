import tensorflow as tf

# 定义两个矩阵常量
matrix1 = tf.constant([[3., 3.]])
matrix2 = tf.constant([[2.], [2.]])

# 两个矩阵乘
product = tf.matmul(matrix1, matrix2)

# 启动计算图
# sess.run 运行计算图
with tf.Session() as sess:
    result = sess.run(product)
    print(result)
