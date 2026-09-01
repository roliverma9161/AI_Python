import pandas as pd
s=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
print(s)
print('By number index',s[0])
print('By number index',s['a'])
