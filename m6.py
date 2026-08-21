import matplotlib.pyplot as plt
names=['group a','group b','group c']
values=[1,10,100]
plt.figure(figsize=(9,3))
plt.subplot(131)#1 row,3col,2index
plt.bar(names,values)

plt.subplot(132)#1 row,3col,2index
plt.scatter(names,values)

plt.subplot(133)#1row,3col,3index
plt.plot(names,values)

plt.suptitle('Categorical plotting')
plt.show()