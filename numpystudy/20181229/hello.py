import numpy as np

# array = np.arange(0, 10)
# print(array.shape)
# print(array.shape())

x = np.random.randint(1, 8, size=5)
print(x.shape)
print(x)

x1 = x[np.newaxis, :]
print(x1.shape)
print(x1)

x2 = x[:, np.newaxis]
print(x2.shape)
print(x2)
