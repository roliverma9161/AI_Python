import  pandas as pd
import numpy as np
df=pd.read_csv("./customers-100.csv")
clean_df=df.dropna()
print(clean_df)
