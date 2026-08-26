import  pandas as pd
import numpy as np
df=pd.read_csv("./customers-100.csv")
mean_value = df['Index'].mean()
print(mean_value)
