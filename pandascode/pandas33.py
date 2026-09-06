import pandas as pd
import numpy as np

#dictionary of lists
dict={'First Score':[100,90,87,95],
      'Second Score':[30,40,56,np.nan],
      'Third Score':[np.nan,40,80,98],
      'Forth Score':[np.nan,np.nan,87,np.nan]}

#creating a dataframe from dictionary
df=pd.DataFrame(dict)

#using dropna()function
print(df.dropna(how='any'))