import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6]])

arr2 = np.array([[6, 5], [4, 3], [2, 1]])

arr3 = np.array([[1, 2, 3], [4, 5]])

# 查看arr维度
print(arr1.shape)  # (2, 3)
print(arr2.shape)  # (3, 2)
print(arr3.shape)  # (2,)

# 切片
print(np.array([1, 2, 3, 4, 5, 6])[:3])  # array([1,2,3])
print(arr1[0:2, 0:2])  # 二维切片

# 乘法
print(np.array([1, 2, 3]) * np.array([2, 3, 4]))  # 对应元素相乘 array([2,6,  12])
print(arr1.dot(arr2))  # 矩阵乘法

# 矩阵求和
print(np.sum(arr1))  # 所有元素之和 21
print(np.sum(arr1, axis=0))  # 列求和 array([5, 7, 9])
print(np.sum(arr1, axis=1))  # 行求和 array([ 6, 15])

# 最大最小
print(np.max(arr1, axis=0))
print(np.min(arr1, axis=1))
