import pandas as pd
dict={'name':['apama','pankaj','sudir','geeku'],
      'degree':['MBA','BCA','M.Tech','MBA'],
      'score':[90,40,80,98]}


df=pd.DataFrame(dict, index=[True,False,True,False])

#accessing a dataframe using .loc[] function
print(df.iloc[1])