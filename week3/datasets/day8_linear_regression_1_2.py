import numpy as np
import matplotlib.pyplot as plt

#공부시간 x1, 과외시간x2
import pandas as pd

data = [[2, 0, 81],[4, 4, 93],[6, 2, 91],[8, 3, 97]]


x1 = [i[0] for i in data] #공부시간
x2 = [i[1] for i in data] #과외시간
y = [i[2] for i in data]

ax = plt.axes(projection='3d')
ax.set_xlabel('study_hour')
ax.set_ylabel('private_class')
ax.set_zlabel('score')
ax.dist = 11
ax.scatter(x1,x2,y)
plt.show()
x1_data = np.array(x1)
x2_data = np.array(x2)
y_data = np.array(y)

#초기 a(기울기) b(y절편)
a1 = 0
a2 = 0
b = 0

#학습률 작아지면 학습하는데 오래걸림.  더 많은 시도 ~~~

lr = 0.05
#몇 번 학습을 진행할지(전체 데이터에 대해 1번씩 진행을 1epochs 라함)
epochs =2001


#겅사하강법 GD
for i in range(epochs):
    y_hat = a1 *x1_data + a2 *x2_data + b
    error = y_data - y_hat #오차를 구하는식

    a1_diff = -(1/len(x1_data))*sum(x1_data *(error))  #오차함수를 a로 미분
    a2_diff = -(1 / len(x2_data)) * sum(x2_data * (error))  # 오차함수를 a로 미분
    d_diff = -(1/len(x1_data))*sum(y_data - y_hat)            #오차함수를 b로 미분

    a1 = a1 - lr * a1_diff #학습률을 곱해 a값업데이트
    a2 = a2 - lr * a2_diff  # 학습률을 곱해 a값업데이트
    b = b - lr * d_diff #학습률을 곱해 b값업데이트
    if i % 100 == 0:
        print('epochs=%.f, 기울기1=%.f,기울기2=%.f, y절편=%.f' %(i, a1, a2, b))

#pip install statsmodels
import  statsmodels.api as statm
import  statsmodels.formula.api as statfa
x = [i[0:2] for i in data]
y = [i[2] for i in data]
x_1 = statm.add_constant(x)
result = statm.OLS(y, x_1).fit()
hour_class = pd.DataFrame(x,columns=['study_hours','private_class'])
hour_class['score']=pd.Series(y)
model = statfa.ols(formula='score ~ study_hours + private_class', data= hour_class)
result_formula= model.fit()
a, b = np.meshgrid(np.linspace(hour_class.study_hours.min()
                               ,hour_class.study_hours.max(),100)
                   ,np.linspace(hour_class.private_class.min(),
                                hour_class.private_class.max(),100))
x_ax = pd.DataFrame({'study_hours':a.ravel(),'private_class':b.ravel()})
fittedY = result_formula.predict(exog=x_ax)
fig=plt.figure()
graph = fig.add_subplot(111, projection='3d')
graph.scatter(hour_class['study_hours'], hour_class['private_class']
              ,hour_class['score'],c='blue',marker='o',alpha=1)
graph.plot_surface(a,b, fittedY.values.reshape(a.shape)
                   ,rstride=1, cstride=1, color='none',alpha=0.4)
graph.set_xlabel('study hour')
graph.set_ylabel('private class')
graph.set_zlabel('socre')
graph.dist=11
plt.show()
