import pandas as pd
df = pd.read_csv('./data/playing golf.csv')
print(df.columns.values.tolist())
train_x = df[['outlook', 'temperature','humidity','windy']]
train_y = df['play']

from sklearn import tree
from sklearn.preprocessing import LabelEncoder
#LabelEncoter 원핫 코딩
enc_class = {}
def encoding_labe(x):
    le = LabelEncoder()
    le.fit(x)
    label = le.transform(x)
    enc_class[x.name] = le.classes_
    return label
train_x = train_x[train_x.columns].apply(encoding_labe)
print(train_x)
#pip install graphviz
model = tree.DecisionTreeClassifier()
model.fit(train_x,train_y) # fit 하면 모델이 생성됨

import graphviz
dot_data = tree.export_graphviz(model, out_file=None
                                ,feature_names=train_x.columns.values.tolist()
                                ,class_names=train_y.drop_duplicates().values.tolist()
                                # ,class_names=['no','yes']
                                ,filled=True, rounded=True
                                ,special_characters=True)
graph = graphviz.Source(dot_data)
graph.render('./golf2', view=True)
print(graph)
print(enc_class.keys())
for i in enc_class.keys():
    print(i,enc_class[i])
print(enc_class['outlook'][[0]] +'흐리면 나감')