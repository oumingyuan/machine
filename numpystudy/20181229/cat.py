import tensorflow as tf

# res = tf.random_uniform((4, 4), -1, 1)
res1 = tf.zeros([1, ])
with tf.Session() as sess:
    print(sess.run(res1))

res2 = tf.zeros([2, 2, ])
with tf.Session() as sess:
    print(sess.run(res2))
