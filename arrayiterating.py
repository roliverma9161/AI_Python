import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8]])
print('simple loop-Print rows')
for row in a:
    print(row)
    print('simple loop-Print each value')
    for row in a:
        for col in row:
            print(col)
            print('nditer()-Print each value')
            for val in np.nditer(a):
                print(val)

                print('ndernumberate()-Print(id,value)')
                for id,val in np.ndenumerate(a):
                 print(id,val)