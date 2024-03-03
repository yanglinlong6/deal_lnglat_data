###求和式
import numpy as np

# Matplotlib 是一个 Python 的 2D绘图库
import matplotlib as mpl
import matplotlib.pyplot as plt

X = np.array([[8, 6, 8], [5, 8, 8], [1, 2, 2], [2, 2, 4], [6, 6, 8], [7, 6, 8]])
Y = np.array([15, 13, 3, 5, 13, 14])
# W1 = (np.random.random(2)-0.5)*2;
W = np.array([0, 0, 0])
lr = 0.002
# 计算迭代次数
n = 0
# #神经网络输出
O1 = 0
O2 = 0
Q = 0
n = 0


def update():
    global X, Y, W, lr, n
    n = n + 1
    O = np.dot(X, W.T)
    O2 = np.dot(X, W.T)
    # Q=np.array([O1,O2]);
    # Q=np.dot(Q,W.T);
    # 计算权值差
    W_Tmp = lr * ((Y - O.T).dot(X))
    W = W + W_Tmp


if __name__ == "__main__":
    for index in range(10000):
        update()
        Q = np.dot(X, W.T)
        print(W)
        print(Q)
        print(Y)
