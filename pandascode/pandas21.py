import pandas as pd
dict={'name':['apama','pankaj','sudir','geeku'],
      'score':[90,40,80,98]}

#creating a dataframe with boolean index
df=pd.DataFrame(dict, index=[True,False,True,False])

#accessing a dataframe using .loc[] function
print(df.loc[True])