import pandas as pd
import numpy as np
df=pd.read_csv("./customers-100.csv")
df['new_City']=df['First Name']+df['Last Name']
print(df)