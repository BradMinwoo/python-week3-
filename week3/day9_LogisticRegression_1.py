import pandas as pd
passengers = pd.read_csv('./data/Titanic Passengers.csv')
print(passengers.columns)

test = passengers[['sex','survived']].groupby('sex', as_index=False).mean().sort_values(by='sex', ascending=False)
print(test)
# female :1, male :0
print(passengers.head())
passengers['sex'] = passengers['sex'].map({'female':1, 'male':0 })
print(passengers.head())
passengers['age'].fillna(value=passengers['age'].mean(), inplace=True)
passengers['firstClass'] = passengers['pclass'].apply(lambda x : 1 if x == 1 else 0)
passengers['secondClass'] = passengers['pclass'].apply(lambda x : 1 if x == 2 else 0)
passengers['thirdClass'] = passengers['pclass'].apply(lambda x : 1 if x == 3 else 0)
print(passengers)

features = passengers[['sex', 'age', 'firstClass', 'secondClass', 'thirdClass']]
survival = passengers[['survived']]

from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = train_test_split(features, survival, test_size=0.2)
print(train_x)

#정규화 (스케일링)
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
train_x = scaler.fit_transform(train_x)
test_x = scaler.fit_transform(test_x)
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(train_x, train_y)

print('학습 데이터 성능 :', model.score(train_x, train_y))
print('테스트 데이터 성능 :' , model.score(test_x, test_y))
print(model.coef_)# a값
print(model.intercept_) #y절편
import  numpy as np
Jack = np.array([0.0, 20.0, 0.0, 0.0, 1.0])
Rose = np.array([1.0, 17.0, 1.0, 0.0, 0.0])
AP = np.array([0.0, 35.0, 0.0, 1.0, 0.0])
AP_BABY= np.array([1.0, 3.0, 0.0, 1.0, 0.0])
sample = np.array([Jack, Rose, AP, AP_BABY])
sample = scaler.transform(sample)

print(model.predict(sample)) #예측
print(model.predict_proba(sample)) #확률