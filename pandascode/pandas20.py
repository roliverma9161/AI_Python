import pandas as pd
RollNo=[101,104,103,102]
d={'Name':['Ajay','Vijay','Sanjay','vikas'],
   'M1':[52,61,57,65]}
#print(d)
df=pd.DataFrame(d,index=RollNo)
sorted_df=df.sort_index()
print(sorted_df)