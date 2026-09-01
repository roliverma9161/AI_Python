import pandas as pd
s=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])

#retrieve a single element
print(s['a'])

#update a single element
s['a']=20
print(s)

#update a single elemnet
s['a']='A'
print(s)