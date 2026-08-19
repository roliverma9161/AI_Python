import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[11,12,13],[14,15,16]])

c=np.concatenate((a,b),axis=0)
print('Array joint at axis=0')
print(c)

c=np.concatenate((a,b),axis=1)
print('Array joint at axis=1')
print(c)

c=np.vstack((a,b))
print('Array join vertically')
print(c)

c=np.vstack((a,b))
print('Array join Horizontally')
print(c)