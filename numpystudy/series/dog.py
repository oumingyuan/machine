import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-1, 1, num=100)
np.random.shuffle(X)  # 将数据集随机化

Y = 0.5 * X + 2 + np.random.normal(0, 0.05, (100,))

# 标准正态分布
Z = np.random.normal(loc=0, scale=1, size=10)

print(X)
print(Y)
plt.scatter(X, Y)
plt.show()
