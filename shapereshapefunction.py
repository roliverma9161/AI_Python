import numpy as np
a=np.array([1,2,3,4,5,6,7,8])
print('Array Before:')
print(a)
print('shape of array',a.shape)

a=a.reshape(2,4)
print('Array After:')
print(a)
print('shape of array',a.shape)

a=np.array([1,2,3,4],[5,6,7,8])
print('Array Before:')
print(a)
a=a.reshape(8)
print('Array After:')
print(a)
print('shape of array',a.shape)


