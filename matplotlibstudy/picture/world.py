# -*- coding: utf-8 -*-
import tensorflow as tf
import matplotlib.pylab as plt

# 读取数据文件
image = tf.read_file("cat/cat.jpg", 'r')
# 将图像文件解码为Tensor
image_tensor = tf.image.decode_jpeg(image)
print(image_tensor)
# 图像张量的形状
shape = tf.shape(image_tensor)
session = tf.Session()
print("图像的形状为：")
print(session.run(shape))
# 将tensor转换为ndarray
image_ndarray = image_tensor.eval(session=session)
print("image_ndarray: " + str(type(image_ndarray)))
print(image_ndarray.shape)
# 显示图片
plt.imshow(image_ndarray)
plt.show()
