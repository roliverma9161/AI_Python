import pandas as pd
from datetime import datetime
import numpy as np
range_date=pd.date_range(start='1/1/2019',end='1/08/2019',freq='min')
df=pd.DataFrame(range_date,columns=['date'])
df['data']=np.random.randint(0,100,size=(len(range_date)))
df['datetime']=pd.to_datetime(df['data'])
df=df.set_index('datetime')
df.drop(['date'],axis=1,inplace=True)
print(df.loc['2019-01-05'].iloc[1:11])