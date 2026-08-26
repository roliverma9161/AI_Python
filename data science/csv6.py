import  pandas as pd
import numpy as np
df=pd.read_csv("./customers-100.csv")
sorted_df=df.sort_values(by='Company')
print(sorted_df)
