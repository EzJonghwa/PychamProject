import matplotlib.pyplot as plt
import numpy as np

def euclidean(x,y):
    return np.sqrt(np.sum((x-y)**2))

a= np.array([1,1])
b = np.array([0,6])

print('거리', euclidean(a,b))
plt.scatter([a[0],b[0],a[1],b[1]])
plt.show()