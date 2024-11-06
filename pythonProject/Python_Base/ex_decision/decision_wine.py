import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# 이탈리아 피에몬테 지역 와인
# class 0 : barolo
# class 1 : grignoline
# class 2 : barbera

np.random.seed(42)
wine = load_wine()
x = wine.data
y= wine.target

x_train, x_test, y_train, y_test = train_test_split(x,y
                        , test_size=0.2, random_state=42)
# tree = DecisionTreeClassifier(criterion='gini', max_depth=3, random_state=42)
tree = DecisionTreeClassifier(criterion='entropy', max_depth=5, random_state=42)
tree.fit(x_train, y_train)
plt.figure(figsize=(16,10))
plot_tree(tree, feature_names=wine.feature_names, class_names=wine.target_names, filled=True, rounded=True, fontsize=10)
plt.title('gini')
plt.show()