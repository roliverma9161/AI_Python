import pandas as pd
import numpy as np
df=pd.read_csv("./customers-100.csv")
df=df.rename(columns={'old_City'})