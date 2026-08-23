import numpy as np
A1=np.array([1,2,3,4,5])
A2=np.array([[1,2,3],[4,5,6]])
A3=np.array([[1,2,3],[4,5,6],[7,8,9]])
#1D Array - A1
print(np.median(A1))

#2D Array - A2
print(np.median(A2))
print(np.median(A2,0))
print(np.median(A2,1))

#2D Array - A3
print(np.median(A3))
print(np.median(A3,0))
print(np.median(A3,1))