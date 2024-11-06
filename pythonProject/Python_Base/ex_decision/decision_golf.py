
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import  LabelEncoder
from sklearn.tree import plot_tree
import pandas as pd

df = pd.read_csv('playing golf.csv')
# le = LabelEncoder()
# print(df.columns)
# df['outlook'] = le.fit_transform(df['outlook'])
# df['temperature'] = le.fit_transform(df['temperature'])
# df['humidity'] = le.fit_transform(df['humidity'])
# df['windy'] = df['windy'].astype(int)
# df['play'] = le.fit_transform(df['play'])
# print(df.head())
x= df[['outlook','temperature', 'humidity', 'windy']]
y= df['play']

enc_class ={}
def encode_label(x):
    le=LabelEncoder()
    le.fit(x)
    label = le.transform(x)
    enc_class[x.name] = le.classes_
    return label
x= x[x.columns].apply(encode_label)
print(x)




x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.5,random_state=0)
model= DecisionTreeClassifier(random_state=0)
model.fit(x_train, y_train)
import matplotlib.pyplot as plt
plt.figure(figsize=(12,8))
plot_tree(model, feature_names=x.columns, class_names=['No','Yes'], filled=True)
acc= model.score(x_test,y_test)
plt.title(f"golf accuracy:{acc:.2f}")
plt.show()
for v in enc_class:
    print(v,enc_class[v])
