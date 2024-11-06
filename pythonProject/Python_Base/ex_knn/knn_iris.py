import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np

# 아이리스 데이터셋
iris = datasets.load_iris()
x = iris.data
y = iris.target
target_names = iris.target_names
# 꽃받침 길이와 너비
plt.figure()
markers = ['o', '^', 's']
for i, (color
 , marker) in enumerate(zip(['navy', 'turquoise','darkorange'],markers)):
    plt.scatter(x[y == i, 0], x[y == i, 1], color=color
                , marker=marker, label=target_names[i])
plt.xlabel('length')
plt.ylabel('width')
plt.legend()
plt.show()



from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

import numpy as np

# 시드값 설정
np.random.seed(1)

x_train , x_test , y_train, y_test = train_test_split(x,y,test_size=0.2)
knn = KNeighborsClassifier()
knn.fit(x_train, y_train)
scores = []

for n in range(1,30):
    knn.n_neighbors=n
    score = knn.score(x_test,y_test)
    scores.append(score)

plt.plot(range(1,30),scores, marker='o')
plt.show()



