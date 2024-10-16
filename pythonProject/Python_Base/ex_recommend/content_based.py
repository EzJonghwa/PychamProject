import numpy as np
import pandas as pd

# cos유사도 를 사용해 고객의 데이터와 비교
def cos_sim(x,y):
    return np.dot(x,y)/ (np.linalg.norm(x)*np.linalg.norm(y))

def fn_sim(user, items):
    sim_arr =[]
    for item in items:
        sim_arr.append(round(cos_sim(user,item),3))
    return sim_arr

df = pd.read_excel('./item_metric.xlsx')
user_metric = [1,0,0.33,0.67,0.67,0.67,0.33,0,0.67,0.33]
item_arr =[]
for i in range (len(df.index)):
    item_arr.append(df.loc[i].tolist())
print(fn_sim(user_metric,item_arr))