import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd
print(os.getcwd())
df = pd.read_csv("./datasets/heights.csv")

x = df['height']
y = df['weight']

plt.figure(figsize=(8, 5))
plt.scatter(x, y)
plt.show()

x_data = np.array(x.round())
y_data = np.array(y.round())

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