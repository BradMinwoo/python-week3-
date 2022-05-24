import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
dataset = np.loadtxt('./data/pima-indians-diabetes.csv'
                     , delimiter = ',')
x = dataset[:, 0:8]
y = dataset[:,8]
train_x, test_x, train_y, test_y = train_test_split(x, y)
scaler = StandardScaler()
train_x = scaler.fit_transform(train_x)
test_x = scaler.transform(test_x)
model = LogisticRegression()
model.fit(train_x, train_y)
print('학습데이터 성능 : ', model.score(train_x, train_y))
print('테스트데이터 성능 : ', model.score(test_x, test_y))
my_data = np.array([0, 180, 88, 41, 235, 30.1, 0.704, 35])
my_data = np.array([my_data])
my_data=scaler.transform(my_data)
print(model.predict(my_data))
print(model.predict_proba(my_data))
