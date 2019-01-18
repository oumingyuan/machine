import numpy as np

'''
可见，它们区别主要在于： 
array会复制出一个新的对象，占用一份新的内存空间，
而as array不会执行这一操作。
array类似深拷贝，as array类似浅拷贝。
'''
np.array([1, 2, 3])  # 创建一维数组
np.asarray([1, 2, 3])
# np.array([1, 2, 3], [4, 5, 6])  # 创建多维数组

# np.zeros((3, 2))  # 3行2列 全0矩阵
# np.ones((3, 2))  # 全1矩阵
# np.full((3, 2), 5)  # 3行2列全部填充5
