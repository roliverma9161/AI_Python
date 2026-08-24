import pandas as pd
import numpy as np

#read csv file into a pandas dataframe
df=pd.read_csv("./customers-100.csv")

#show the first 5 rows of the dataframe
print(df.head())