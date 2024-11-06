import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
df = pd.read_csv('./data/Mall_Customers.csv')
df['Gender']=  df['Gender'].map({'Female':1, "Male":0})
data = df[['Gender', 'Age', 'Annual Income', 'Spending Score']]
# 그룹에 포함된 데이터간에 퍼짐 정도를 inertia
# inertia가 낮은 군집이 좋은 군집
inertia= []
cnt =list(range(1,11))
for i in range(1, 11):
    model= KMeans(n_clusters=i)
    model.fit(data)
    inertia.append(model.inertia_)
plt.plot(cnt, inertia, '-0')
plt.xlabel('clusters(k)')
plt.ylabel('inertia')
plt.show()

