import numpy as np
import matplotlib.pyplot as plt

# x: 공부시간 y: 힙격(1)/불합격(0)
x = np.array([2,4,6,8,10,12,14])
y = np.array([0,0,0,1,1,1,1])

a= 0 # 기울기
b = 0 # y절편
lr = 0.05 # 학습률
epochs =2001
plt.scatter(x,y)


def sigmoid(x):
    return 1/ (1 + np.exp(-x))
n = len(x)
for i in range(epochs):
    y_pred = sigmoid(a * x+b)       # 예측값
    error = y - y_pred              # 오차
    a_diff = -(1/n) *sum(x*error)   # a,b에 대한 기울기 편 미분
    b_diff = -(1/n) * sum(error)
    a =a -lr * a_diff               #
    b =b -lr * b_diff
    if i%100 ==0:
        print(f"epochs={i}, a={a}, b={b}")
x_range = np.arange(0,15,0.1)
plt.plot(x_range,sigmoid(a*x_range+b))
plt.show()