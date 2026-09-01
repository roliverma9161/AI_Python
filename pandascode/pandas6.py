import pandas as pd
data={'a':0,'b':1,'c':2,}
s=pd.Series(data)
print(s)
s1=pd.Series(data,index=['a','b','c'])
print(s1)
s1=pd.Series(data,index=[0,1,2])#pulled out
print(s1)