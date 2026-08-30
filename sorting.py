import numpy as np
t=np.array([10,20,30,'red'])
[21,31,41,'green']
[50,60,70,'brown']
[89,97,11,'green']
row=np.where(t=='green')
print(row)
