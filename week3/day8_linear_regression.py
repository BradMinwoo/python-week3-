import numpy as np
import matplotlib.pyplot as plt

data = [[2, 81],[4, 93],[6, 91],[8,97] ]
x = [i[0] for i in data]
y = [i[1] for i in data]

plt.figure(figsize=(8, 5))
plt.scatter(x, y)
plt.show()

#초기 a(기울기) b(y절편)
a = 0
b = 0
#학습률 작아지면 학습하는데 오래걸림.  더 많은 시도 ~~~


lr = 0.01
#몇 번 학습을 진행할지(전체 데이터에 대해 1번씩 진행을 1epochs 라함)
epochs =2001

x_data = np.array(x)
y_data = np.array(y)
#겅사하강법 GD
for i in range(epochs):
    y_hat = a *x_data + b
    error = y_data - y_hat #오차를 구하는식

    a_diff = -(1/len(x_data))*sum(x_data *(error))  #오차함수를 a로 미분
    d_diff = -(1/len(x_data))*sum(error)            #오차함수를 b로 미분

    a = a - lr * a_diff #학습률을 곱해 a값업데이트
    b = b - lr * d_diff #학습률을 곱해 b값업데이트
    if i % 100 == 0:
        print('epochs=%.f, 기울기=%.f, y절편=%.f' %(i, a, b))
y_pred= a*x_data + b
plt.scatter(x, y)
plt.plot([min(x_data),max(x_data)], [min(y_pred),max(y_pred)])
plt.show()