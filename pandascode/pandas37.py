import pandas as pd

data={'Name':['jai','princi','gaurav','Anuj'],
      'Age':[27,24,22,32],
      'Address':['Nagpur','Kanpur','Allahabad','Knnuaj'],
      'qualification':['Msc','MA','MCA','PHD']}

df=pd.DataFrame(data)
df.dropna(inplace=True)
df["Address"]=df["Address"].str.split("a")
print(df)