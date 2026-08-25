import numpy as np
x=np.random.rand()

#randaom number from 0-1
print(x)
#0.60494724

x=np.random.randint(100)
#A number from 1-100

print(x)

x=np.random.choice([1,2,3,4,5])
print(x)
#3

#Arrays of random numbers
x=np.random.randint(100, size=(2,3))
print(x)

#Array of 5 random number from0-1
x=np.random.rand(2,3)
print(x)

x=np.random.choice([1,2,3,4,5],size=(2,3))
print(x)