import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#pip install sklearn 앞에 햇던 수학적 방법말로 라이브러리로 실행
#pip install matplotlib
data = [[2, 81],[4, 93],[6, 91],[8,97] ]
x = [i[0] for i in data]
y = [i[1] for i in data]

plt.figure(figsize=(8, 5))
plt.scatter(x, y)
plt.show()

x_data = np.array(x)
y_data = np.array(y)

line_model = LinearRegression()
print(x_data)
print(x_data.reshape(-1,1))
line_model.fit(x_data.reshape(-1, 1), y_data) # 데이터로 모델 학습 : fit
print('공부시간 5기간으로 예측', line_model.predict([[5]])) # 모델 예측
print(line_model.coef_) #기을기
print(line_model.intercept_) #y절펄
plt.plot(x_data.reshape(-1,1), y_data,'o')
plt.plot(x_data.reshape(-1,1), line_model.predict(x_data.reshape(-1, 1)))
plt.show()