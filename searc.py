import numpy as np
a=np.array([1,4,3,2,8,7,6])
print('values of Array-A')
print(a)
print('sorted Array:')
print(np.sort(a))
print('search the even number')
x=np.where(a==2)
print(x)
