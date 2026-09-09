import pandas as pd

data={'Name':['jai','princi','gaurav','Anuj'],
      'Age':[27,24,22,32],
      'Address':['Nagpur junction','Kanpur junction','Allahabad junction','Knnuaj junction'],
      'qualification':['Msc','MA','MCA','PHD']}

df=pd.DataFrame(data)

new=df["Address"].replace("Nagpur junction","Nagpur junction").copy()

print(new.str.strip()=="Nagpur junction")
print(new.str.strip()=="Nagpur junction")
print(new.str.strip()=="Nagpur junction")