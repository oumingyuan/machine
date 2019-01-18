# 最小二乘法试验
import numpy as np
from scipy.optimize import leastsq
import matplotlib.pyplot as plt

# 采样点(Xi,Yi)
Xi = np.array([8.19, 2.72, 6.39, 8.71, 4.7, 2.66, 3.78])
Yi = np.array([7.01, 2.78, 6.47, 6.71, 4.1, 4.23, 4.05])

i = 0


# 需要拟合的函数func及误差error
def func(p, x):
    k, b = p
    return k * x + b


def error(p, x, y):
    global i

    i = i + 1
    print('error函数执行次数：' + str(i))

    return func(p, x) - y  # x、y都是列表，故返回值也是个列表


def get_value():
    # TEST
    p0 = np.array([1000, 20000])
    # print( error(p0,Xi,Yi) )

    # 主函数从此开始
    # 把error函数中除了p以外的参数打包到args中
    para = leastsq(error, p0, args=(Xi, Yi))
    k, b = para[0]
    # print("k=", k, '\n', "b=", b)
    print("y = %sx + %s" % (k, b))

    return {'k': k, 'b': b}


# 绘图，看拟合效果
def write_picture(param):
    plt.figure(figsize=(8, 6))
    plt.scatter(Xi, Yi, color="red", label="Sample Point", linewidth=3)  # 画样本点
    x = np.linspace(0, 10, 1000)
    y = param['k'] * x + param['b']
    plt.plot(x, y, color="orange", label="Fitting Line", linewidth=1)  # 画拟合直线
    plt.legend()
    plt.show()


result = get_value()
write_picture(result)
