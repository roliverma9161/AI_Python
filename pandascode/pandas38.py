import pandas as pd

data={'Name':['jai','princi','gaurav','Anuj'],
      'Age':[27,24,22,32],
      'Address':['Nagpur','Kanpur','Allahabad','Knnuaj'],
      'qualification':['Msc','MA','MCA','PHD']}

df=pd.DataFrame(data)
print(df)
df["Age"]=df["Age"].replace(25,"Twenty five")
print(df)