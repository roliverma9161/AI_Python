import pandas as pd
import numpy as np
df=pd.read_csv("./customers-100.csv")
Index_sum=df['Index-name'].sum()
print(Index_sum)