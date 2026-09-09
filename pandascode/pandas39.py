import pandas as pd

data={'Name':['jai','princi','gaurav','Anuj'],
      'Age':[27,24,22,32],
      'Address':['Nagpur','Kanpur','Allahabad','Knnuaj'],
      'qualification':['Msc','MA','MCA','PHD']}

df=pd.DataFrame(data)

new=df['Address'].copy()
df["Name"]=df["Name"].str.cat(new,sep=",")
print(df)