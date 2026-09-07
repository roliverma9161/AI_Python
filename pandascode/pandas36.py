import pandas as pd

data={'Name':['jai','princi','gaurav','Anu'],
      'Age':[27,24,22,32],
      'Addresss':['Delhi','Kanpur','Allahabad','Kannau'],
      'qualification':['Msc','MA','MCA','PHD']}

df=pd.DataFrame(data)

df['Name']=df['Name'].str.lower()
print(df)