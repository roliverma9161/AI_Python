import  pandas as pd
import numpy as np
df=pd.read_csv("./customers-100.csv")
df2=pd.read_csv("./entries.csv")
merged_df=pd.merge(df, df2, on='Index')
print(merged_df.head())