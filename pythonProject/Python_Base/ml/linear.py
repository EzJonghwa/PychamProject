import numpy as np
import matplotlib.pyplot as plt

# 공부한 시간 x, 성적 y
x = np.array([2,4,6,8])
y= np.array([81,93,91,97])
plt.scatter(x,y)
# plt.show()

# 기울기 a, y절편 b
a = 0
b = 0

# 학습률 (런닝 메이트 결정)
lr =0.03

# 몇번 반복할지(에포크) 4개가 한번실행하는것이 1에포크 for문으 돌릴 예정이라 2001번 실행
epochs =2001

# x 값이 총 몇개인지
n =len(x)

for i in range(epochs):
    y_pred = a*x+b # 예측을 구하는 식
    error = y-y_pred
    a_diff = (2/n) * sum(-x*(error)) # 오차를 구하는 함수를 a 로 편미분
    b_diff =(2/n) * sum(-(error))
    a= a-lr * a_diff  # 학습률을 곱해 기존의 a 값을 업데이트
    b= b-lr * b_diff  # 학습률을 곱해 기존의 b 값을 업데이트
    # 편미분이란 ? 여러 변수에 의해 정의된 함수애서 하나의 변수에 대해 미분 하는 것
    # 나머지 변수는 고정 시키고, 특정 변수 하나에 대해서만 함수가 어떻게 변하는지 알아보는
    # 이 함수가 변수 x에 대해 어떻게 변하는지, y에 대해 어떻게 변하는지.
    if i % 100 ==0:
        print(f"epoch={i}, 기울기 a ={a}, y절편={b}")
# 최적의 a,b
y_pred = a * x +b
# plt.scatter(x,y)
plt.plot(x,y_pred, 'r')
plt.show()