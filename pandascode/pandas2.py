import pandas as pd
fruits=['apple','orange','mango','pear']
quantities=[20,30,52,15]
S=pd.Series(quantities,index=fruits)
print(S)