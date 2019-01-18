# 调用模块
from sklearn.datasets import load_iris

load_data = load_iris()

# 导入数据和标签
data_X = load_data.data
data_y = load_data.target

print(data_y)
