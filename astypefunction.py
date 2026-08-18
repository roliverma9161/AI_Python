import numpy as np
a=np.array([1.1,2.5,0.6,4.7,5.3])
print('values of Array')
print(a)
print('data type of Array:',a.dtype)

a=a.astype("i")
print('values of Array')
print(a)
print('data type of Array:',a.dtype)

a=a.astype("bool")
print('values of Array')
print(a)
print('data type of Array:',a.dtype)

