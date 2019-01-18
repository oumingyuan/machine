import numpy as np

'''
https://blog.csdn.net/zhangergou0628/article/details/80436491
'''


def linear_regression(data_x, data_y, learning_rate, loop_num):
    w, b = 0, 0

    # 梯度下降
    for i in range(loop_num):
        w_derivative, b_derivative, cost = 0, 0, 0
        for j in range(len(data_x)):
            wx_plusb = w * data_x[j] + b
            w_derivative += (wx_plusb - data_y[j]) * data_x[j]
            b_derivative += wx_plusb - data_y[j]
            cost += (wx_plusb - data_y[j]) * (wx_plusb - data_y[j])
        w_derivative = w_derivative / len(data_x)
        b_derivative = b_derivative / len(data_x)

        w = w - learning_rate * w_derivative
        b = b - learning_rate * b_derivative

        cost = cost / (2 * len(data_x))
        if i % 100 == 0:
            print(cost)
    print('w:', w)
    print('b:', b)


if __name__ == "__main__":  # _x:protected  __x:private
    x = np.random.normal(0, 10, 100)
    noise = np.random.normal(0, 0.05, 100)
    y = 2 * x + 7 + noise
    linear_regression(x, y, 0.01, 5000)
