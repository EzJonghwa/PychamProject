from sklearn import datasets
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sympy.abc import alpha

iris= datasets.load_iris()
label= pd.DataFrame(iris.target)
label.columns=['labels']
data =pd.DataFrame(iris.data)
# sepal 꽃받침, petal 꽃잎
data.columns= ['Sepal length', 'Sepal width', 'Petal length', 'Petal width']
data= pd.concat([data, label], axis=1)
print(data.head())
# kMeans <-- K: 군집의 수
model = KMeans(n_clusters=3)
x_data = data[['Petal length','Petal width']]
model.fit(x_data) # 비지도 학습(정답 데이터 없이 학습함)
pred= pd.DataFrame(model.predict(x_data))
pred.columns=['predict']
all_data = pd.concat([data, pred], axis=1)

# 시각화
plt.scatter(all_data['Petal length'], all_data['Petal width'],
            c=all_data['predict'],alpha=0.5)
center= pd.DataFrame(model.cluster_centers_
                     , columns=['Petal length', 'Petal width'])
plt.scatter(center['Petal length'], center['Petal width'], s=50,marker='D', c='r')
plt.show()
