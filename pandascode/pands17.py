import pandas as pd
d={'Name':["ram","shyam","uma","dinesh"],'Age':[28,34,29,42]}
df=pd.DataFrame(d, index=['e1','e2','e3','e4'])
print(df)
#retrieving row by loc method

first=df.loc['e1']
second=df.loc['e2']
first=df.iloc[2]
second=df.iloc[3]