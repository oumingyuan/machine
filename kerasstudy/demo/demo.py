from keras.models import Sequential
from keras.layers import Dense
import numpy as np

# 最简单的模型
model = Sequential()

# 堆叠模型
model.add(Dense(units=64, activation='relu', input_dim=1))
model.add(Dense(units=1, activation='softmax'))

# 配置学习过程
model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])

# 创建数据集
x_batch = np.linspace(-1, 1, num=200)
np.random.shuffle(x_batch)  # 将数据集随机化
y_batch = 0.5 * x_batch + 2 + np.random.normal(0, 0.05, (200,))
# 喂数据
model.train_on_batch(x_batch, y_batch)

W, b = model.layers[0].get_weights()

print(W, b)

loss_and_metrics = model.evaluate(x_batch, y_batch, batch_size=128)
