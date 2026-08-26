import  pandas as pd
import numpy as np
df=pd.read_csv("./customers-100.csv")
group_city=df.groupby("City")["Name"].count()
print(group_city)
