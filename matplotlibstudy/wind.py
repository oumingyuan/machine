import matplotlib.pyplot as plt

'''
函数图像
'''
# 使用列表数据作为坐标轴
age = [5, 10, 15, 20, 25, 30]

height = [25, 45, 65, 75, 75, 75]

plt.plot(age, height)

plt.title('Age vs Height')

plt.xlabel('age')

plt.ylabel('Height')

plt.show()
