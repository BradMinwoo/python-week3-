from os import pread

import numpy as np
import  matplotlib.pylab as plt

# data = [[2,81],[4,93],[6,91],[8,97]]
# 공시간에 따른 합격 불합격
data = [[2, 0], [4, 0], [6, 0], [8, 1], [10, 1], [12, 1], [14, 1]]
#가상의 기울기 와 y절편
x= [i[0] for i in data]
y = [i[1] for i in data]

plt.scatter(x, y)
plt.xlim(0, 15)
plt.ylim(-.1, 1.1)
# plt.show()

# 초기 a(기울기) b(y절편)
a= 0
b= 0

# 학습률
lr = 0.05
def sigmoid(x):
    return 1 / (1 + np.e ** (-x))

for i in range(2001):
    for x_data, y_data in data:
        a_diff = x_data * (sigmoid(a * x_data + b) - y_data)
        b_diff = sigmoid(a * x_data + b) - y_data
        a = a - lr * a_diff
        b = b - lr * b_diff
        if i % 100 == 0:
            print("epoch=%.f, 기울기=%.04f, 절편=%.f" % (i, a, b))
plt.scatter(x, y)
plt.xlim(0, 15)
plt.ylim(-.1, 1.1)

x_range = (np.arange(0, 15, 0.1)) # 그래프 나타낼 x값의 범위
plt.plot(np.arange(0, 15, 0.1), np.array([sigmoid(a * x + b) for x in x_range]))
plt.show()