import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6]])

# 布尔型数组访问方式
print((arr > 2))
"""
[[False False]
 [ True  True]
 [ True  True]]
"""
print(arr[arr > 2])  # [3 4 5 6]

# 修改形状
print("修改形状")
print(arr.reshape(2, 3))
"""    
array([[1, 2, 3],
   [4, 5, 6]])
"""
print(arr.flatten())  # 摊平 array([1, 2, 3, 4, 5, 6])
print(arr.T)  # 转置
